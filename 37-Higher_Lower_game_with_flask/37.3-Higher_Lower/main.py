from flask import Flask, redirect, url_for
from random import randint

app = Flask(__name__)
random_num = randint(0, 9)

@app.route("/")
def greet():
    return '<h1>Guess a number between 0 and 9</h1>' \
            '<img src = "https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"/>'

@app.route("/<int:number>")
def check(number):
    if number > random_num:
        return redirect(url_for("higher"))
    elif number < random_num:
        return redirect(url_for("lower"))
    else:
        return redirect(url_for("correct"))
        
@app.route("/lower")
def lower():
    return '<h1>Too low!</h1>' \
            '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"/>'
            
@app.route("/higher")
def higher():
    return '<h1>Too high!</h1>' \
            '<img src = "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"/>'

@app.route("/correct")
def correct():
    return '<h1>You found me!</h1>' \
            '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"/>'
app.run(debug=True)