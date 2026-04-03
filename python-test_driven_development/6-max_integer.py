#!/usr/bin/python3
"""Module that contains a function to find the max integer in a list."""


def max_integer(list=[]):
    """Returns the max integer in a list.

    Args:
        list (list): list of integers

    Returns:
        int: maximum integer or None if list is empty
    """
    if len(list) == 0:
        return None
    result = list[0]
    for item in list[1:]:
        if item > result:
            result = item
    return result
