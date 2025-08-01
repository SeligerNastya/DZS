import math
import sqlite3
import time

class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def get_menu(self):
        sql = "SELECT * FROM mainmenu"
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res
        except IOError:
            print("Ошибка чтения из БД")
        return []

    def add_contact(self, name, text):
        try:
            tm = math.floor(time.time())
            self.__cur.execute("INSERT INTO posts VALUES(NULL, ?, ?, ?)", (name, text, tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print("Ошибка добавления отзыва БД" + str(e))
            return False
        return True

    def get_contact(self, contact_id):
        try:
            self.__cur.execute(f"SELECT name, text FROM posts WHERE id = {contact_id}")
            res = self.__cur.fetchone()
            if res:
                return res
        except sqlite3.Error as e:
            print("Ошибка получения отзыва из БД" + str(e))
        return False, False
    def get_posts_anonce(self):
        try:
            self.__cur.execute("SELECT id, name, text FROM posts ORDER BY time DESC")
            res = self.__cur.fetchall()
            if res:
                return res
        except sqlite3.Error as e:
            print("Ошибка получения статьи из БД" + str(e))
        return []