#!/usr/bin/python3
# defining a FileStorage class
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    # representing an abstracted storage engine

    # Attributes:
    # __file_path : a name of the file to save objects to
    # __objects : a dictionary of instantiated objects

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        # returning a dictionary of instantiated objects in objects
        if cls is not None:
            if type(cls) == str:
                cls = eval(cls)
            cls_dict = {}
            for k, v in self.__objects.items():
                if type(v) == cls:
                    cls_dict[k] = v
            return cls_dict
        return self.__objects

    def new(self, obj):
        # setting in objects obj with key <obj_class_name.id
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        # serializing objects to the JSON file file_path
        odict = {o: self.__objects[o].to_dict() for o in self.__objects.keys()}
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(odict, f)

    def reload(self):
        # deserializing JSON file file_path to objects
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                for o in json.load(f).values():
                    name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(name)(**o))
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        # deleting a given object from objects
        try:
            del self.__objects["{}.{}".format(type(obj).__name__, obj.id)]
        except (AttributeError, KeyError):
            pass

    def close(self):
        # calling the reload method
        self.reload()
