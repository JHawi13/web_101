from flask import Flask
from flask import Flask,render_template

app=Flask(__name__) #creates a wsgi server

@app.route("/")
def home_page():
    return render_template('index.html')

@app.route("/Interest")
def interest():
    return "<h1>interest</h1>"
