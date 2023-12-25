#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv


class DBStorage:
    """This class manages storage of hbnb models in Database """
    __engine = None
    __session = None

    def __init__(self):
        """ initialisation """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)
        # Base.metadata.create_all(self.__engine)
        Base.metadata.create_all(self.__engine)
        """# self.__session = scoped_session(sessionmaker(bind=self.__engine,
        #                                             # expire_on_commit=False))"""

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        classes = {
               'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'State': State, 'City': City, 'Amenity': Amenity,
               'Review': Review
              }
        temp_dict = {}
        """
        if cls:
            objects = self.__session.query(classes[cls]).all()"""
        if cls:
            class_name = cls.__name__
            objects = self.__session.query(classes[class_name]).all()
        else:
            all_classes = list(classes.values())
            objects = []
            for c in all_classes:
                objects.extend(self.__session.query(c).all())
        for obj in objects:
            key = f"{obj.__class__.__name__}.{obj.id}"
            temp_dict[key] = obj
        return temp_dict

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.__session.add(obj)

    def save(self):
        """Saves storage dictionary to file"""
        self.__session.commit()

    def reload(self):
        """Loads storage dictionary from file"""
        Base.metadata.create_all(self.__engine)
        sessions = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(sessions)

    def delete(self, obj=None):
        """ delete obj from __objects if it’s inside
            if obj is equal to None, the method should not do anything"""
        if obj is None:
            return
        elif obj:
            self.__session.delete(obj)

    def close(self):
        """ """
        self.__session.close()
