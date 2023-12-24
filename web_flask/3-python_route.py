#!/usr/bin/python3
""" Starts a Flash Web Application """

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    """ display “Hello HBNB!” """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """ display “HBNB” """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def C_is_fun(text):
    """
        display “C ” followed by the value of the text variable
        (replace underscore _ symbols with a space )
    """
    text_space = text.replace("_", " ")
    return f"C {text_space}"


@app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text):
    """
    display “Python ”, followed by the value of the text variable
    (replace underscore _ symbols with a space )
    """

    text_space2 = text.replace("_", " ")
    return f"Python {text_space2}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
