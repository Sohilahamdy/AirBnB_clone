#!/usr/bin/env python3
import cmd

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """End of File command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def do_help(self, line):
        """Override to provide help information"""
        cmd.Cmd.do_help(self, line)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
