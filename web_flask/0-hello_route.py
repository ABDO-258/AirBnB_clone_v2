#!/usr/bin/python3
""" flask init """

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_HBNB():
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run()
