#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    """
    Class HBNBCommand that implements the command interpreter
    """
    def __init__(self):
        """
        Initialize the class with the prompt and empty objects list
        """
        super().__init__()
        self.prompt = "(hbnb) "

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
