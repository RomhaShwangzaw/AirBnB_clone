#!/usr/bin/python3
''' The console module '''

import cmd


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
