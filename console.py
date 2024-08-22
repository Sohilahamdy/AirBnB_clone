#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the AirBnB project.
    This class handles the command line interface for managing
    AirBnB objects. It supports commands like quit, EOF, and help.
    """

    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, line):
        """Exit the program when EOF (Ctrl+D) is encountered."""
        return True

    def do_help(self, line):
        """Display help information about commands."""
        if line:
            # Display help for a specific command
            if hasattr(self, 'do_' + line):
                func = getattr(self, 'do_' + line)
                print(self._get_help(func))
            else:
                print("*** No help on {}".format(line))
        else:
            # Display the default help information
            super().do_help(line)

    def emptyline(self):
        """Override the emptyline method to do nothing
           on an empty input line."""
        pass

    def _get_help(self, func):
        """Helper method to get the help string for a command function."""
        doc = func.__doc__
        return doc if doc else "No help available."


if __name__ == '__main__':
    HBNBCommand().cmdloop()
