#!/usr/bin/python3
""" flask web app"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.city import City

app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def HBNB_filters():
    """
    display a HTML page
    """
    states = storage.all(State)
    amenities = storage.all(Amenity)
    places = storage.all(Place)
    cities = storage.all(City)

    return render_template('100-hbnb.html',
                           states=states, amenities=amenities,
                           places=places, cities=cities)


@app.teardown_appcontext
def teardown_app(self, exception=None):
    """ remove the current SQLAlchemy Session """
    storage.close()


if __name__ == '__main__':
    app.run()
