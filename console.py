#!/usr/bin/python3

import os
import sys
import json
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb) '
    classes = {
        'BaseModel': BaseModel, 'User': User, 'City': City,
        'Place': Place, 'Amenity': Amenity, 'Review': Review,
        'State': State
    }

    def do_quit(self, arg):
        exit()

    def do_EOF(self, arg):
        print('')
        exit()

    def emptyline(self):
        pass

    def do_create(self, arg):

        if not arg:
            print('** class name missing **')
            return

        class_name = arg.split()[0]
        if class_name not in self.classes:
            print(f"** class '{class_name}' doesn't exist **")
            return

        new_instance = self.classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):

        if not arg:
            print('** class name missing **')
            return

        class_name = arg.split()[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        if len(arg.split()) > 1:
            key = f"{class_name}.{arg.split()[1]}"
            if key in storage.all():
                print(storage.all()[key])
            else:
                print('** no instance found **')
        else:
            print('** instance id missing **')

    def do_destroy(self, arg):

        if not arg:
            print("** class name missing **")
            return

        class_name = arg.split()[0]
        try:
            obj = eval(class_name)
        except Exception:
            print("** class doesn't exist **")
            return

        if len(arg.split()) == 1:
            print('** instance id missing **')
            return

        key = f"{class_name}.{arg.split()[1]}"
        if key in storage.all():
            storage.all().pop(key)
            storage.save()
        else:
            print('** no instance found **')
            return

    def do_all(self, arg):

        if not arg:
            print([str(a) for a in storage.all().values()])
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            print([str(a) for b, a in storage.all().items() if arg in b])

    def do_update(self, arg):
        arg = arg.split()

        if not arg:
            print('** class name missing **')
            return

        class_name = arg[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        if len(arg) == 1:
            print('** instance id missing **')
            return

        key = f"{class_name}.{arg[1]}"
        if key in storage.all():
            if len(arg) > 2:
                if len(arg) == 3:
                    print('** value missing **')
                else:
                    setattr(storage.all()[key], arg[2], arg[3][1:-1])
                    storage.all()[key].save()
            else:
                print('** attribute name missing **')
        else:
            print('** no instance found **')


if __name__ == '__main__':
    HBNBCommand().cmdloop()
