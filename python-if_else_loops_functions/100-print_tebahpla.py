#!/usr/bin/python3
alphabet = ""
for alpha in range(ord('a'), ord('z') + 1):
    if alpha % 2 == 1:
        alphabet += chr(alpha - 32)
    else:
        alphabet += chr(alpha)

print("{}".format(alphabet[::-1]), end="")
