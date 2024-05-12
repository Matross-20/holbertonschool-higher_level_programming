#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arguments = sys.argv
    num_of_arg = len(arguments)

    if num_of_arg > 1:
        if num_of_arg == 2:
            arg = "argument:"
        else:
            arg = "arguments:"
        print("{} {}" .format(num_of_arg - 1, arg))
        for i in range(1, num_of_arg):
            print("{}: {}" .format(str(i), arguments[i]))

    else:
        print("{} arguments." .format(num_of_arg - 1))
