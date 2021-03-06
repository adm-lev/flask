from re import T
import time
import math
import sqlite3
from flask import url_for




class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def getMenu(self):
        sql = '''SELECT * FROM mainmenu'''
        try:            
            self.__cur.execute(sql)
            
            res = self.__cur.fetchall()
            if res: return res
        except:
            print('Read error from DB')
        return []

    def addPost(self, title, text, url):
        try:
            self.__cur.execute(f"SELECT COUNT() as `count` FROM posts WHERE url LIKE '{url}'")
            res = self.__cur.fetchone()
            if res['count'] > 0:
                print('this url already exist')
                return False

            tm = math.floor(time.time())
            self.__cur.execute("INSERT INTO posts VALUES(NULL, ?, ?, ?, ?)", (title, text, url, tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print(f'Error adding {str(e)}')
            return False

        return True  

    def getPost(self, alias):
        try:
            self.__cur.execute(f'SELECT title, text FROM posts WHERE url LIKE "{alias}" LIMIT 1')
            res = self.__cur.fetchone()
            if res:
                base = url_for('static', filename='images') 
                return res 
        except sqlite3.Error as e:
            print(f'Error getting data {str(e)}')
        return (False, False) 

    def getPostsAnonce(self):
        try:
            self.__cur.execute(f'SELECT id, title, text, url FROM posts ORDER BY time DESC')
            res = self.__cur.fetchall()
            
            if res: return res
        except sqlite3.Error as e:
            print(f'Error getting data {str(e)}')
        return []

    def addUser(self, name, email, hpsw):
        try:
            self.__cur.execute(f"SELECT COUNT() as `count` FROM users WHERE email LIKE '{email}'")
            res = self.__cur.fetchone()
            if res['count'] > 0:
                print('user with this email is olready exist')
                return False

            tm = math.floor(time.time())
            self.__cur.execute('INSERT INTO users VALUES(NULL, ?, ?, ?, NULL, ?)', (name, email, hpsw, tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print(f'error {e}')
            return False

        return True

    def getUser(self, user_id):
        try:
            self.__cur.execute(f'SELECT * FROM users WHERE id = {user_id} LIMIT 1')
            res = self.__cur.fetchone()
            if not res:
                print('user doesnt found')
                return False

            return res
        except sqlite3.Error as e:
            print(f'error giving data from bd {str(e)}')

        return False

    def getUserByEmail(self, email):
        try:
            self.__cur.execute(f"SELECT * FROM users WHERE email LIKE '{email}' LIMIT 1")
            res = self.__cur.fetchone()
            if not res:
                print('user not found')
                return False

            return res
        except sqlite3.Error as e:
            print(f'yoyo error getting data from db {str(e)}')

        return False