#!/usr/bin/python3
def uppercase(str):
    result = 0
    for i in range(len(str)):
        if str[i] >= 'a' and str[i] <= 'z':
            result = ord(str[i]) - 32
        else:
            result = ord(str[i])
        print(chr(result), end="")

    print("")
