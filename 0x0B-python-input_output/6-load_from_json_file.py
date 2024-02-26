#!/usr/bin/python3
"""Defines a function that creates object fron JSON."""
import json


def load_from_json_file(filename):
    """Create a Python object from a JSON file."""
    with open(filename) as a:
        return json.load(a)
