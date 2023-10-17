#!/usr/bin/python3
"""script for adding item in json list"""


from sys import argv
import json


save_to_json = __import__('5-save_to_json').save_to_json
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if __name__ == "__main__":
    try:
        json_list = load_from_json_file('add_item.json')
    except FileNotFoundError:
        json_list = []

    for i in range(len(argv)):
        json_list.append(argv[i])
    save_to_json(json_list, "add_item.json")
