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
import re

class HBNBCommand(cmd.Cmd):
    """
    Class HBNBCommand that implements the command interpreter
    """
    prompt = "(hbnb) "
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
    def default(self, line):
        """Catch commands if nothing else matches then."""
        # print("DEF:::", line)
        self._precmd(line)

    def _precmd(self, line):
        """Intercepts commands to test for class.syntax()"""
        # print("PRECMD:::", line)
        match = re.search(r"^(\w*)\.(\w+)(?:\(([^)]*)\))$", line)
        if not match:
            return line
        classname = match.group(1)
        method = match.group(2)
        args = match.group(3)
        match_uid_and_args = re.search('^"([^"]*)"(?:, (.*))?$', args)
        if match_uid_and_args:
            uid = match_uid_and_args.group(1)
            attr_or_dict = match_uid_and_args.group(2)
        else:
            uid = args
            attr_or_dict = False

        attr_and_value = ""
        if method == "update" and attr_or_dict:
            match_dict = re.search('^({.*})$', attr_or_dict)
            if match_dict:
                self.update_dict(classname, uid, match_dict.group(1))
                return ""
            match_attr_and_value = re.search(
                '^(?:"([^"]*)")?(?:, (.*))?$', attr_or_dict)
            if match_attr_and_value:
                attr_and_value = (match_attr_and_value.group(
                    1) or "") + " " + (match_attr_and_value.group(2) or "")
        command = method + " " + classname + " " + uid + " " + attr_and_value
        self.onecmd(command)
        return command

    def update_dict(self, classname, uid, s_dict):
        """Helper method for update() with a dictionary."""
        s = s_dict.replace("'", '"')
        d = json.loads(s)
        if not classname:
            print("** class name missing **")
        elif classname not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(classname, uid)
            if key not in storage.all():
                print("** no instance found **")
            else:
                attributes = storage.attributes()[classname]
                for attribute, value in d.items():
                    if attribute in attributes:
                        value = attributes[attribute](value)
                    setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()

    def do_count(self, argument):
        """  retrieve the number of instances of a class """
        tokensA = shlex.split(argument)
        dic = models.storage.all()
        num_instances = 0
        if tokensA[0] not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            for key in dic:
                className = key.split('.')
                if className[0] == tokensA[0]:
                    num_instances += 1

            print(num_instances)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
