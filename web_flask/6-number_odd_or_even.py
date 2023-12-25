#!/usr/bin/python3
""" flask init """

from flask import Flask, render_template

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


@app.route("/number/<int:n>", strict_slashes=False)
def python_number(n):
    """ display “n is a number” only if n is an integer """
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def python_number_page(n):
    """ display a HTML page only if n is an integer """
    return render_template('5-number.html', num=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def python_number_odd_even(n):
    """ display a HTML page only if n is an integer """
    if n % 2 == 0:
        num = f"{n} is even"
    else:
        num = f"{n} is odd"
    return render_template('6-number_odd_or_even.html', num=num)


if __name__ == '__main__':
    app.run()
