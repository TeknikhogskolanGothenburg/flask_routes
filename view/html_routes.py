from view import app

from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.errorhandler(404)
def handler404(_):
    return render_template('404.html')