#!/usr/bin/python3
""" flask web app"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def HBNB_states():
    """
    display a HTML page with the list of all State objects in DBStorage
    """
    states = storage.all('State')
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def HBNB_states_id(id):
    """
    display a HTML page with the list of all State objects in DBStorage
    """
    states = storage.all('State')
    for state in states.values():
        print(state)
        print(type(state))
        if state.id == id:
            return render_template('9-states.html', states_id=state)
    return render_template('9-states.html', state_id=None)


@app.teardown_appcontext
def teardown_app(self, exception=None):
    """ remove the current SQLAlchemy Session """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
