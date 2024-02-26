#!/usr/bin/python3
"""Defines a function thst inserts text."""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing a given string in a file.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for within the file.
        new_string (str): The string to insert.
    """
    text = ""
    with open(filename) as a:
        for line in a:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as b:
        b.write(text)
