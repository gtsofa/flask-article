# app.py

import os

from flask import Flask, render_template
from data import Articles

app = Flask(__name__)

Articles = Articles()

# home route
@app.route('/')
def index():
    #return 'Tsofa, karibu!'
    return render_template('home.html')
    
# about route
@app.route('/about')
def about():
    return render_template('/about.html')
    
# articles route
@app.route('/articles')
def articles():
    return render_template('/articles.html', articles = Articles)
    
# dynamic articles route
@app.route('/article/<string:id>/')
def article(id):
    return render_template('/article.html', id = id)


if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))#c9