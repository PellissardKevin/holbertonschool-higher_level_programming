#!/usr/bin/python3
import sys
argv = sys.argv

if __name__ == "__main__":
    if len(argv) <= 1:
        print("{} arguments.".format(len(argv) - 1))
    else:
        print("{} arguments:".format(len(argv) - 1))
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))
