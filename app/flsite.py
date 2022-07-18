from config import Configuration
from flask import Flask, render_template, url_for, request, flash


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
            flash('message sent')
        else:
            flash('send error')
        print(request.form)
    return render_template('contactus.html', title='callback', menu=menu)



if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000)


