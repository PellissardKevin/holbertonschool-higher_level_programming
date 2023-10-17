#!/usr/bin/python3
"""Definition of write function"""


def write_file(filename="", text=""):
    with open(filename, "w", encoding='utf-8') as file:
        return file.write(text)

