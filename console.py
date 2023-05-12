#!/usr/bin/python3
"""
This is the console model
it provides the entry to the console with
some specific implementations
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
    """provides the entry point to the imterpreter"""

    prompt = "(hbnb) "
    my_classes = {"BaseModel", "User", "State", "City",
                  "Amenity", "Place", "Review"}

    def do_quit(self, s):
        """this implements the quit"""
        return True

    def do_EOF(self, s):
        """this implements the EOF"""
        print()
        return True

    def help_quit(self):
        """the implements the help for quit"""
        print("Quit command to exit the program\n")

    def help_EOF(self):
        """this implements the help for EOF"""
        print("EOF command to exit the program\n")

    def emptyline(self):
        """this overrides the empty line default method"""
        pass

    def do_create(self, s):
        """Creates a new instance of BaseModel, Saves it and prints the id"""
        if len(s) == 0:
            print("** class name missing **")
        elif s not in HBNBCommand.my_classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(s)()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, s):
        """Prints the string rep of an instance"""
        if len(s) == 0:
            print("** class name missing **")
            return
        args = list(s.split())
        if args[0] not in HBNBCommand.my_classes:
            print("** class doesn't exist **")
            return
        try:
            classname = f"{args[0]}.{args[1]}"
            if classname not in storage.all().keys():
                print("** no instance found **")
            else:
                print(storage.all()[classname])
        except IndexError:
            print("** instance id missing **")

    def do_destroy(self, s):
        """Deletes an Instance based on the class name and id"""
        if len(s) == 0:
            print("** class name missing **")
            return
        args = list(s.split())
        if args[0] not in HBNBCommand.my_classes:
            print("** class doesn't exist **")
            return
        try:
            classname = f"{args[0]}.{args[1]}"
            if classname not in storage.all().keys():
                print("** no instance found **")
            else:
                del storage.all()[classname]
                storage.save()
        except IndexError:
            print("** instance id missing **")

    def do_all(self, s):
        """Prints all the objects or objects a particular class"""
        obj_lists = []
        args = list(s.split())
        if len(s) == 0:
            for keys in storage.all().values():
                obj_lists.append(keys)
            print(obj_lists)
        elif s in HBNBCommand.my_classes:
            for key, value in storage.all().items():
                if s in key:
                    obj_lists.append(value)
            print(obj_lists)
        else:
            print("** class doesn't exist **")

    def do_update(self, s):
        """Updates as instance based on the class name and id"""
        args = list(s.split())
        classname = f"{args[0]}.{args[1]}"
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.my_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif classname not in storage.all().keys():
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            attr_value = args[3]
            attr_value = attr_value.strip('"')
            attr_value = attr_value.strip("'")
            casting = type(eval(args[3]))
            setattr(storage.all()[classname], args[2], casting(attr_value))
            storage.all()[classname].save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
