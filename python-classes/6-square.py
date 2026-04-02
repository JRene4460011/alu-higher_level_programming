#!/usr/bin/python3
"""6-square.py"""


class Square:
    """Defines a square with size and position."""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size          # triggers the size setter
        self.position = position  # triggers the position setter

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square with validation."""
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(n, int) for n in value) or
            not all(n >= 0 for n in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square using '#' considering position."""
        if self.__size == 0:
            print()
            return

        # print vertical offset
        for _ in range(self.__position[1]):
            print()

        # print each square row
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
