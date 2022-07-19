from crypt import methods
from unicodedata import category

# from requests import session
from config import Configuration
from flask import Flask, render_template, url_for, request, session, flash, redirect, abort


app = Flask(__name__)
app.config.from_object(Configuration)



menu = [{'name': 'install', 'url':'install-flask'},
        {'name': 'firat app', 'url': 'fitst-app'},
        {'name': 'contactus', 'url': 'contact'}]


@app.route('/')
def index():
    print(url_for('index'))
    return render_template('index.html', menu=menu)


@app.route('/about')
def about():
    print(url_for('/about'))
    return render_template('about.html', title='about site', menu=menu)


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        if len(request.form['username']) > 2:
            flash('message sent', category='success')
        else:
            flash('send error', category='error')
        print(request.form)
    return render_template('contactus.html', title='callback', menu=menu)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if 'userLogged' in session:
        return redirect(url_for('profile', username=session['userLogged']))
    elif request.method == 'POST' and request.form['username'] == 'eugene' and request.form['psw'] == '123':
        session['userLogged'] = request.form['username']
        return redirect(url_for('profile', username=session['userLogged']))

    return render_template('login.html', title='Authorisation', menu=menu)


@app.route('/profile/<username>')
def profile(username):
    if 'userLogged' not in session or session['userLogged'] != username:
        abort(401)
    return f"{username}'s profile"



@app.errorhandler(404)
def pageNotFound(error):
    return render_template('page404.html', title='Page not found', menu=menu), 404



if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000)


