from config import Configuration
from flask import Flask, render_template, url_for


app = Flask(__name__)
app.config.from_object(Configuration)


menu = ['install', 'first app', 'callback']


@app.route('/')
def index():
    print(url_for('index'))
    return render_template('index.html', menu=menu)


@app.route('/about')
def about():
    print(url_for('/about'))
    return render_template('about.html', title='about site', menu=menu)



if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000)


