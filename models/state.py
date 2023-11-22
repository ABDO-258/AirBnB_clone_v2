#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel):
    """ State class """
    __tablename__ = "States"
    name = Column(String(128), nullable=False)

    # For DBStorage
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", backref="state",
                              cascade="all, delete-orphan")

    # For FileStorage
    else:
        @property
        def cities(self):
            from models import storage
            city_list = []
            for city in storage.all("City").values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
