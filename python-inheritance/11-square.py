#!/usr/bin/python3
"""11-square module"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class inheriting from Rectangle"""

    def __init__(self, size):
        """Initialize a square with a given size

        Args:
            size (int): size of the square (validated)
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Return the string representation of the square"""
        return "[Square] {}/{}".format(self.__size, self.__size)

    def area(self):
        """Return the area of the square"""
        return self.__size * self.__size
