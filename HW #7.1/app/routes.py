
from flask import render_template
from app import app
import random

@app.route('/test')
def test(): # xxx add the view function for the test link here
    a = 'author'
    b = 'body'
    u = 'username'
    cities = ["Portland", "San Jose"] + ['San Francisco', 'New York', 'Chicago', 'Philadelphia', 'Boston']
    names = ["Joe", "Jessie", "Jonnason", "John", "Sue", "Susie", "Susan" ]
    n = 3
    posts = []
    for i in range (n): # create random posts
        s = 'The best city in US to live is ' + random.choice(cities) + "!!!"
        name = random.choice(names)
        d = {a : {u : name }, b: s }
        posts.append(d)
    user = { u: 'Folks'}
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/')
@app.route('/index' )
def index():
    a = 'author'
    b = 'body'
    u = 'username'
    user = { u: 'Miguel'}
    posts = [
        {
            a: {u: 'John'},
            b : 'Beautiful day in Portland!'
        },
        {
            a: {u: 'Susan'},
            b : 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
