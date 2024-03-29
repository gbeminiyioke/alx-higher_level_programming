#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Body of the class Square."""

    def __init__(self, size=0):
        """Square class contructor.

        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size mist be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
