from crypt import methods
from statistics import mode
from unicodedata import category
import os
import sqlite3
# from requests import session
from config import Configuration
from flask import Flask, render_template, url_for, request, session, flash, redirect, abort, g, redirect
from FDataBase import FDataBase
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.config.from_object(Configuration)


app.config.update(dict(DATABASE=os.path.join(app.root_path, 'flsite.db')))

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

dbase = None

@app.before_request
def before_request():

    global dbase
    db = get_db()
    dbase = FDataBase(db)


@app.route('/')
def index():
    
    return render_template('index.html', menu=dbase.getMenu(), posts=dbase.getPostsAnonce())

@app.route('/add_post', methods=['POST', 'GET'])
def addPost():
    

    if request.method == 'POST':
        if len(request.form['name']) > 4 and len(request.form['post']) > 10:
            res = dbase.addPost(request.form['name'], request.form['post'], request.form['url'])
            if not res:
                flash('Error adding page', category='error')
            else:
                flash('Article added!', category='success')
        else:
            flash('Error adding page', category='error')

    return render_template('add_post.html', menu=dbase.getMenu(), title='Adding page')

@app.route('/post/<alias>')
def showPost(alias):
    
    title, post = dbase.getPost(alias)
    if not title:
        abort(404)

    return render_template('post.html', menu=dbase.getMenu(), title=title, post=post)

@app.route('/login', methods=['POST', 'GET'])
def login():
    return render_template('login.html', menu=dbase.getMenu(), title='Authorisation')

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        if len(request.form['name']) > 4 and len(request.form['email']) > 4 \
            and len(request.form['psw']) > 4 and request.form['psw'] == request.form['psw2']:
            hash = generate_password_hash(request.form['psw'])
            res = dbase.addUser(request.form['name'], request.form['email'], hash)
            if res:
                flash('register sucseed')
                return redirect(url_for('login'))
            else:
                flash('register fail')
        else:
            flash('wrong field info')

    return render_template('register.html', menu=dbase.getMenu(), title='Registration')


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()





if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000)












































# app = Flask(__name__)
# app.config.from_object(Configuration)



# menu = [{'name': 'install', 'url':'install-flask'},
#         {'name': 'firat app', 'url': 'fitst-app'},
#         {'name': 'contactus', 'url': 'contact'}]


# @app.route('/')
# def index():
#     print(url_for('index'))
#     return render_template('index.html', menu=menu)


# @app.route('/about')
# def about():
#     print(url_for('/about'))
#     return render_template('about.html', title='about site', menu=menu)


# @app.route('/contact', methods=['POST', 'GET'])
# def contact():
#     if request.method == 'POST':
#         if len(request.form['username']) > 2:
#             flash('message sent', category='success')
#         else:
#             flash('send error', category='error')
#         print(request.form)
#     return render_template('contactus.html', title='callback', menu=menu)


# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     if 'userLogged' in session:
#         return redirect(url_for('profile', username=session['userLogged']))
#     elif request.method == 'POST' and request.form['username'] == 'eugene' and request.form['psw'] == '123':
#         session['userLogged'] = request.form['username']
#         return redirect(url_for('profile', username=session['userLogged']))

#     return render_template('login.html', title='Authorisation', menu=menu)


# @app.route('/profile/<username>')
# def profile(username):
#     if 'userLogged' not in session or session['userLogged'] != username:
#         abort(401)
#     return f"{username}'s profile"



# @app.errorhandler(404)
# def pageNotFound(error):
#     return render_template('page404.html', title='Page not found', menu=menu), 404



# if __name__ == '__main__':

#     app.run(host='0.0.0.0', port=5000)


