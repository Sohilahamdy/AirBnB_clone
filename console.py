#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    """Command interpreter for AirBnB"""

    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Exit the program on EOF"""
        return True

    def do_help(self, line):
        """Display help information for commands"""
        super().do_help(line)

    def emptyline(self):
        """Override empty line handling"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
