from http.cookiejar import debug

from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'drffghgdescxvQ3RQGNBGDGF'

menu = [
    {"name": "Главная", "url": "index"},
    {"name": "О нас", "url": "about"},
    {"name": "Номера", "url": "rooms"},
    {"name": "Контакты", "url": "contact"}
]


@app.route("/")
@app.route("/index")
def index():
    return render_template( "index.html", title="Главная", menu=menu)

@app.route("/about")
def about():
    return render_template( "about.html", title="О нас", menu=menu)

@app.route("/rooms")
def rooms():
    return render_template( "rooms.html", title="Номера", menu=menu)

@app.route("/contact")
def contact():
    return render_template("contact.html", title="Контакты", menu=menu)

@app.errorhandler(404)
def page_not_found(error):
    return render_template("page.html", title="Страница не найдена", menu=menu)





if __name__ == '__main__':
    app.run(debug=True)