#!/usr/bin/python3
"""
Class HBNBCommand that implements the command interpreter
"""

import cmd
import shlex
import sys
import models
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    """
    Class HBNBCommand that implements the command interpreter
    """
    prompt = "(>>>>) "
    classes = {'BaseModel': BaseModel, 'User': User, 'Amenity': Amenity, 'State': State,
           'Place': Place, 'Review': Review}

    def do_quit(self, line):
        """
        Exit the program
        """
        return True

    def do_EOF(self, line):
        """
        Exit the program
        """
        return True

    def emptyline(self):
        """
        Do nothing when an empty line is entered
        """
        pass

    def do_help(self, line):
        """
        Provide help for commands
        """
        print("Quit the program: quit or EOF")
        
    def do_create(self, argument):
        """Create a new instance of BaseModel, save it (to the JSON file) and print the id."""
        if argument:
            if argument in self.classes:
                # instance = models.base_model.BaseModel()
                get_class = getattr(sys.modules[__name__], argument)
                instance = get_class()
                print(instance.id)
                models.storage.save()
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")
        return
    
    def do_show(self, args):
        """Prints the string representation of an instance based on the class name and id."""
        if not args:
            print("** class name missing **")
            return
        args = args.split()
        if len(args) < 2:
            print("** instance id missing **")
            return
        class_name = args[0]
        if class_name not in models.classes:
            print("** class doesn't exist **")
            return
        model_id = args[1]
        models_dict = models.storage.all()
        key = "{}.{}".format(class_name, model_id)
        if key not in models_dict:
            print("** no instance found **")
            return
        print(models_dict[key])
    
    def do_destroy(self, args):
        """Deletes an instance based on the class name and id (save the change into the JSON file)."""
        if not args:
            print("** class name missing **")
            return
        args = shlex.split(args)
        if len(args) < 2:
            print("** instance id missing **")
            return
        class_name = args[0]
        if class_name not in models.classes:
            print("** class doesn't exist **")
            return
        model_id = args[1]
        models_dict = models.storage.all()
        key = "{}.{}".format(class_name, model_id)
        if key not in models_dict:
            print("** no instance found **")
            return
        del models_dict[key]
        models.storage.save()
        
    def do_all(self, args):
        """Prints all string representation of all instances based or not on the class name."""
        models_dict = models.storage.all()
        if args:
            class_name = args.split()[0]
            if class_name not in models.classes:
                print("** class doesn't exist **")
                return
            print([str(v) for k, v in models_dict.items() if k.startswith(class_name + ".")])
        else:
            print([str(v) for v in models_dict.values()])
    
    def do_update(self, argument):
        """Updates an instance based on the class name and id """
        tokensU = shlex.split(argument)
        if len(tokensU) == 0:
            print("** class name missing **")
            return
        elif len(tokensU) == 1:
            print("** instance id missing **")
            return
        elif len(tokensU) == 2:
            print("** attribute name missing **")
            return
        elif len(tokensU) == 3:
            print("** value missing **")
            return
        elif tokensU[0] not in self.classes:
            print("** class doesn't exist **")
            return
        keyI = tokensU[0] + "." + tokensU[1]
        dicI = models.storage.all()
        try:
            instanceU = dicI[keyI]
        except KeyError:
            print("** no instance found **")
            return
        try:
            typeA = type(getattr(instanceU, tokensU[2]))
            tokensU[3] = typeA(tokensU[3])
        except AttributeError:
            pass
        setattr(instanceU, tokensU[2], tokensU[3])
        models.storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
