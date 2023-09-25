#!/usr/bin/python3
for number in range(0, 100):
    if number == 99:
        print("{:02}".format(int(number)))
    else:
        print("{:02}, ".format(int(number)), end="")
