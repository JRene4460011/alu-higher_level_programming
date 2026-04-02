#!/usr/bin/python3
"""This module defines a square with size getter and setter."""


class Square:
    """Represents a square with a private size and validation."""

    def __init__(self, size=0):
        """Initialize a square with optional size."""
        self.size = size  # Will call the setter for validation

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

    def area(self):
        """Return the current square area."""
        return self.__size ** 2
