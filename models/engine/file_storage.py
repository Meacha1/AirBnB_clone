import json
from datetime import datetime

class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to instances"""

    __file_path = "file.json" # This is the path to the JSON file
    __objects = {} # Empty dictionary to store objects later

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets obj in __objects with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        json_objects = {}
        for key in self.__objects:
            json_objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w") as f:
            f.write(json.dumps(json_objects))

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r") as f:
                json_objects = json.loads(f.read())
                for key in json_objects:
                    class_name = key.split(".")[0]
                    self.__objects[key] = eval(class_name)(**json_objects[key])
        except FileNotFoundError:
            pass
