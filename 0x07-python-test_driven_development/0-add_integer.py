#!/usr/bin/python3
"""Defines a function that adds 2 integers."""


def add_integer(a, b=98):
    """Returns an integer: addition of a and b.

    If arguments are floats, they are typecasted to ints before addition is performed.

    Raises:
        TypeError: If a or b is a non-integer and non-float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
