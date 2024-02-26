#!/usr/bin/python3
"""Defines a function that wrotes an object."""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using JSON representation."""
    with open(filename, "w") as a:
        json.dump(my_obj, a)
