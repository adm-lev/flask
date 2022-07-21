from flask_login import UserMixin
from flask import url_for


class UserLogin(UserMixin):

    def fromDB(self, user_id, db):
        self.__user = db.getUser(user_id)
        return self

    def create(self, user):
        self.__user = user
        return self

    def get_id(self):
        return str(self.__user['id'])

    def getName(self):
        return self.__user['name'] if self.__user else 'without name'

    def getEmail(self):
        return self.__user['email'] if self.__user else 'without email'

    def getAvatar(self, app):
        img = None
        if not self.__user['avatar']:
            try:
                with app.open_resource(app.root_path + url_for('static', filename='images/default.png'), 'rb') as f:
                    img = f.read()
            except FileNotFoundError as e:
                print(f'not found image: {str(e)}')
        else:
            img = set.__user['avatar']

        return img