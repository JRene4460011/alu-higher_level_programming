#!/usr/bin/python3
"""4-inherits_from module"""


def inherits_from(obj, a_class):
    """Return True if obj is instance of subclass of a_class (not a_class itself)"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
