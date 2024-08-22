#!/usr/bin/python3

import cmd
import sys
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command interpreter class for the AirBnB clone"""

    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Exit on EOF"""
        print()
        return True

    def do_create(self, line):
        """Create a new instance of BaseModel, save it, and print the id"""
        if not line:
            print("** class name missing **")
            return
        try:
            cls = eval(line)
            if not issubclass(cls, BaseModel):
                print("** class doesn't exist **")
                return
            instance = cls()
            instance.save()
            print(instance.id)
        except Exception:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Show the string representation of an instance"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            cls = eval(args[0])
            if not issubclass(cls, BaseModel):
                print("** class doesn't exist **")
                return
            if len(args) == 1:
                print("** instance id missing **")
                return
            instance_id = args[1]
            key = f"{args[0]}.{instance_id}"
            instance = storage.all().get(key)
            if instance is None:
                print("** no instance found **")
            else:
                print(instance)
        except Exception:
            print("** class doesn't exist **")

    def do_destroy(self, line):
        """Destroy an instance based on the class name and id"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            cls = eval(args[0])
            if not issubclass(cls, BaseModel):
                print("** class doesn't exist **")
                return
            if len(args) == 1:
                print("** instance id missing **")
                return
            instance_id = args[1]
            key = f"{args[0]}.{instance_id}"
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")
        except Exception:
            print("** class doesn't exist **")

    def do_all(self, line):
        """Show all instances or instances of a specific class"""
        args = line.split()
        if len(args) > 1:
            print("** class doesn't exist **")
            return
        try:
            if len(args) == 0:
                instances = storage.all().values()
            else:
                cls = eval(args[0])
                if not issubclass(cls, BaseModel):
                    print("** class doesn't exist **")
                    return
                instances = [str(instance) for key, instance in storage.all().items() if key.startswith(args[0])]
            print([str(instance) for instance in instances])
        except Exception:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Update an instance based on the class name and id by adding or updating an attribute"""
        args = line.split(' ', 3)
        if len(args) < 3:
            if len(args) < 1:
                print("** class name missing **")
            elif len(args) < 2:
                print("** instance id missing **")
            elif len(args) < 3:
                print("** attribute name missing **")
            return
        try:
            cls = eval(args[0])
            if not issubclass(cls, BaseModel):
                print("** class doesn't exist **")
                return
            if len(args) < 4:
                print("** value missing **")
                return
            instance_id = args[1]
            key = f"{args[0]}.{instance_id}"
            instance = storage.all().get(key)
            if instance is None:
                print("** no instance found **")
                return
            attribute_name = args[2]
            attribute_value = args[3].strip('"')
            if hasattr(instance, attribute_name):
                attr_type = type(getattr(instance, attribute_name))
                setattr(instance, attribute_name, attr_type(attribute_value))
                instance.save()
            else:
                print("** attribute name missing **")
        except Exception:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
