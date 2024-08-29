#!/usr/bin/python3
"""
This module contains the HBNBCommand class, which serves as the
command interpreter for the AirBnB clone project.
It allows users to interact with the application via commands like
'create', 'show', 'destroy', 'all', and 'update'.
"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command interpreter class for the AirBnB clone"""

    prompt = "(hbnb) "

    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Review": Review
    }

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
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        cls = HBNBCommand.classes[class_name]
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
        if class_name not in HBNBCommand.classes:
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
        if class_name not in HBNBCommand.classes:
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
            if class_name not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            instances = [str(instance) for key,
                         instance in storage.all().items()
                         if key.startswith(class_name)]
        print([str(instance) for instance in instances])

    def do_update(self, line):
        """Update an instance based on the class name and
         id by adding or updating an attribute"""
        args = line.split(' ', 3)
        if len(args) < 1:
            print("** class name missing **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        class_name, instance_id, attribute_name, attribute_value = (
           args[0], args[1], args[2], args[3].strip('"')
        )
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        key = "{}.{}".format(class_name, instance_id)
        instance = storage.all().get(key)
        if instance is None:
            print("** no instance found **")
            return
        setattr(instance, attribute_name, attribute_value)
        instance.save()

    def do_count(self, line):
        """Print the count of all class instances"""
        if '.' in line:
            parts = line.split('.')
            class_name = parts[0]
            method_name = parts[1]
            if method_name != "count()":
                print("*** Unknown syntax:", line)
                return
        else:
            class_name = line.strip()

        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        count = 0
        for obj in storage.all().values():
            if obj.__class__.__name__ == class_name:
                count += 1
        print(count)

    def emptyline(self):
        """Do nothing on empty input line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
