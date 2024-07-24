#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    """Command interpreter for the AirBnB project."""
    
    prompt = "(hbnb) "
    
    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, line):
        """Exit the program when EOF (Ctrl+D) is encountered."""
        print("")
        return True

    def do_help(self, line):
        """Display help information about commands."""
        super().do_help(line)

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
