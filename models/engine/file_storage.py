#!/usr/bin/python3

import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State

class FileStorage:

    _file_path = "file.json"
    _objects = {}

    def all(self):
        return FileStorage._objects

    def new(self, obj):
        if obj:
            key = "{}.{}".format(obj._class_._name_, obj.id)
            FileStorage._objects[key] = obj

    def save(self):
        new_dict = {}
        for key, value in FileStorage._objects.items():
            new_dict[key] = value.to_dict().copy()
        with open(FileStorage._file_path, mode='w') as my_file:
            json.dump(new_dict, my_file)

    def reload(self):
        try:
            with open(FileStorage._file_path, mode='r') as my_file:
                new_dict = json.load(my_file)
                for key, value in new_dict.items():
                    class_name = value.get('_class_')
                    obj = eval(class_name + '(**value)')
                    FileStorage._objects[key] = obj
        except FileNotFoundError:
            pass
