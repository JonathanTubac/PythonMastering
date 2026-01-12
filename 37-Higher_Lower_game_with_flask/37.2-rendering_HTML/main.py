from flask import Flask

app = Flask(__name__)

@app.route("/")
def greet():
    return '<h1>Hello!</h1>' \
            '<p>Welcome to this page!</p>' \
            '<img src = "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExbHJ5cW1yNDgyNHl2ZG90aHJlMzF3c2c4Z20yOXdqMm9uYXNtazNtMSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/6lq3SYVbwt5oWFeF2i/giphy.gif" width="200"/>'

@app.route("/bye")
def bye():
    return "Bye"

app.run(debug=True)