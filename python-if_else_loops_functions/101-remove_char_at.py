#!/usr/bin/python3

def remove_char_at(str, n):
    dump_str = ""
    for letter in range(0, len(str)):
        if letter != n:
            dump_str += str[letter]

    return dump_str
