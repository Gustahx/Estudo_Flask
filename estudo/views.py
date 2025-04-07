from estudo import app
from flask import render_template, url_for



@app.route('/')
def homepage():
    user = "Anonymous"
    age = 22

    context = {
        'user': user,
        'age': age
    }
    return render_template('index.html' , context=context)


@app.route('/contact/')
def newpage():
    return "another view"