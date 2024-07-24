#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    """Command interpreter for the AirBnB project.
    
    This class handles the command line interface for managing 
    AirBnB objects. It supports commands like quit, EOF, and help.
    """
    
    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program.

        Usage: quit
        """
        return True

    def do_EOF(self, line):
        """Exit the program when EOF (Ctrl+D) is encountered.

        Usage: EOF
        """
        return True

    def do_help(self, line):
        """Display help information about commands.

        Usage: help [command]
        """
        super().do_help(line)

    def emptyline(self):
        """Override the emptyline method to do nothing on an empty input line."""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
