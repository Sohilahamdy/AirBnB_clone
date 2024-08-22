#!/usr/bin/python3

import cmd
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
        class_name = line.strip()
        if class_name not in globals() or not issubclass(globals()[class_name], BaseModel):
            print("** class doesn't exist **")
            return
        cls = globals()[class_name]
        instance = cls()
        instance.save()
        print(instance.id)

    def do_show(self, line):
        """Show the string representation of an instance"""
        args = line.split()
        if len(args) < 2:
            if len(args) < 1:
                print("** class name missing **")
            else:
                print("** instance id missing **")
            return
        class_name, instance_id = args[0], args[1]
        if class_name not in globals() or not issubclass(globals()[class_name], BaseModel):
            print("** class doesn't exist **")
            return
        key = "{}.{}".format(class_name, instance_id)
        instance = storage.all().get(key)
        if instance is None:
            print("** no instance found **")
        else:
            print(instance)

    def do_destroy(self, line):
        """Destroy an instance based on the class name and id"""
        args = line.split()
        if len(args) < 2:
            if len(args) < 1:
                print("** class name missing **")
            else:
                print("** instance id missing **")
            return
        class_name, instance_id = args[0], args[1]
        if class_name not in globals() or not issubclass(globals()[class_name], BaseModel):
            print("** class doesn't exist **")
            return
        key = "{}.{}".format(class_name, instance_id)
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, line):
        """Show all instances or instances of a specific class"""
        args = line.split()
        if len(args) > 1:
            print("** class doesn't exist **")
            return
        if len(args) == 0:
            instances = storage.all().values()
        else:
            class_name = args[0]
            if class_name not in globals() or not issubclass(globals()[class_name], BaseModel):
                print("** class doesn't exist **")
                return
            instances = [str(instance) for key, instance in storage.all().items() if key.startswith(class_name)]
        print([str(instance) for instance in instances])

    def do_update(self, line):
        """Update an instance based on the class name and id by adding or updating an attribute"""
        args = line.split(' ', 3)
        if len(args) < 4:
            if len(args) < 1:
                print("** class name missing **")
            elif len(args) < 2:
                print("** instance id missing **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            return
        class_name, instance_id, attribute_name, attribute_value = args[0], args[1], args[2], args[3].strip('"')
        if class_name not in globals() or not issubclass(globals()[class_name], BaseModel):
            print("** class doesn't exist **")
            return
        key = "{}.{}".format(class_name, instance_id)
        instance = storage.all().get(key)
        if instance is None:
            print("** no instance found **")
            return
        setattr(instance, attribute_name, attribute_value)
        instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
