from flask import Flask

app = Flask(__name__)

@app.route("/username/<name>/<int:years>")
def greet(name, years):
    return f"Hello {name}, you have {years} working with us!"

app.run(debug=True)