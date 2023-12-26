#!/usr/bin/python3
""" flask web app"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def HBNB_states_list():
    """
    display a HTML page with the list of all State objects in DBStorage
    """
    states = storage.all('State')
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_app(self, exception=None):
    """ remove the current SQLAlchemy Session """
    storage.close()


if __name__ == '__main__':
    app.run()
