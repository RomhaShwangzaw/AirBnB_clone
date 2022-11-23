#!/usr/bin/python3
''' The console module '''

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    ''' The HBNB console class '''

    prompt = '(hbnb) '

    def emptyline(self):
        ''' an empty line + ENTER shouldn’t execute anything '''
        pass

    def do_quit(self, arg):
        ''' Quit command to exit the program '''
        return True

    def do_EOF(self, arg):
        ''' EOF signal to exit the program '''
        print()
        return True

    def do_create(self, arg):
        ''' Usage: create <class>
        Create a new class instance and print its id.
        '''
        if not arg:
            print("** class name missing **")
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            obj = BaseModel()
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        ''' Usage: show <class> <id>
        Display the string representation of a class instance of a given id.
        '''
        objdict = storage.all()
        args = parse(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(args[0], args[1])])

    def do_destroy(self, arg):
        ''' Usage: destroy <class> <id>
        Delete a class instance of a given id.
        '''
        objdict = storage.all()
        args = parse(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in objdict:
            print("** no instance found **")
        else:
            del objdict["{}.{}".format(args[0], args[1])]
            storage.save()

    def do_all(self, arg):
        ''' Usage: all or all <class>
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects.
        '''
        objdict = storage.all()
        if not arg:
            print([str(v) for v in objdict.values()])
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            print([str(v) for k, v in objdict.items()
                  if k.split('.')[0] == arg])

    def do_update(self, arg):
        ''' Usage: update <class> <id> <attribute name> <attribute value>
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair.
        '''
        objdict = storage.all()
        args = parse(arg)

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in objdict:
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            obj = objdict["{}.{}".format(args[0], args[1])]
            if hasattr(obj, args[2]):
                type_attr = type(getattr(obj, args[2]))
                setattr(obj, args[2], type_attr(args[3]))
            else:
                setattr(obj, args[2], args[3])
            obj.save()


def parse(arg):
    return arg.split()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
