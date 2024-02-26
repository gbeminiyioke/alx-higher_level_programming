#!/usr/bin/python3
"""Defines a class-checking function."""


def is_same_class(obj, a_class):
    """Check if an object is exactly a class instance.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match obj type to.
    Returns:
        True If obj is exactly an instance of a_class.
        Otherwise returns False.
    """
    if type(obj) == a_class:
        return True
    return False
