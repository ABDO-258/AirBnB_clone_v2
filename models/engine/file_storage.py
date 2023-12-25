#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    @property
    def cities(self):
        """Retruns Cities in state"""

    def delete(self, obj=None):
        """loop through __objects, compare each value
        of key with cls argument wich is object
        """
        if obj:
            id = obj.to_dict()["id"]
            className = obj.to_dict()["__class__"]
            keyName = className+"."+id
            if keyName in FileStorage.__objects:
                del (FileStorage.__objects[keyName])
                self.save()

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        temp_dict = {}
        if cls:
            if type(cls) == str:
                cls = eval(cls)
            for key, value in FileStorage.__objects.items():
                if type(value) == cls:
                    temp_dict[key] = value
            return temp_dict
        else:
            return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def close(self):
        """ call reload() method for deserializing the JSON file to objects"""
        self.reload()
