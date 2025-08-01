import sqlite3
import os
from flask import Flask, render_template, request, g, flash, abort
from fdatabase import FDataBase

DATABASE = '/tmp/flsite.db'
DEBUG = True
SECRET_KEY = 'ghffffgsj,kedf546578ujh'

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path,'flsite.db')))

def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn
def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()

def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db

@app.route("/")
def index():
    db = get_db()
    dbase = FDataBase(db)
    return render_template( 'index.html',  menu=dbase.get_menu(),posts=dbase.get_posts_anonce())

@app.route("/about")
def about():
    db = get_db()
    dbase = FDataBase(db)
    return render_template( 'about.html',  menu=dbase.get_menu())

@app.route("/rooms")
def rooms():
    db = get_db()
    dbase = FDataBase(db)
    return render_template( 'rooms.html', menu=dbase.get_menu())

@app.route("/add_contact", methods=["POST", "GET"])
def add_contact():
    db = get_db()
    dbase = FDataBase(db)
    if request.method == "POST":
        if len(request.form["name"]) > 3 and len(request.form["post"]) > 10:
            res = dbase.add_contact(request.form["name"],request.form["post"])
            if not res:
                flash("Ошибка добавления отзыва", category="error")
            else:
                flash("Отзыв добавлена успешно", category="success")
        else:
            flash("Ошибка добавления отзыва", category="error")

        return render_template('add_contact.html', menu=dbase.get_menu())
    return render_template('add_contact.html', menu=dbase.get_menu())

@app.route("/contact/<int:id_contact>")
def show_post(id_contact):
    db = get_db()
    dbase =FDataBase(db)
    name,  post = dbase.get_contact(id_contact)
    if not name:
        abort(404)

    return render_template('contact.html', menu=dbase.get_menu(), name=name, post=post)

@app.errorhandler(404)
def page_not_found(error):
    db = get_db()
    dbase = FDataBase(db)
    return render_template("page404.html", title="Страница не найдена", menu=dbase.get_menu())

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


if __name__ == '__main__':
    app.run()