#!/usr/bin/python3
"""Module that contains a function to add two integers."""


def add_integer(a, b=98):
    """Adds two integers or floats (floats are cast to integers).

    Args:
        a (int or float): first number
        b (int or float): second number (default 98)

    Raises:
        TypeError: If a or b is not an int or float.

    Returns:
        int: sum of a and b
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
