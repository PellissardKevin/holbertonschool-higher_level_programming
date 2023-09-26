#!/usr/bin/python3
def uppercase(str):
    result = 0
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            result = ord(i) - 32
        else:
            result = ord(i)
        print("{}".format(chr(result)), end="")
    print("")
    return
