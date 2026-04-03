#!/usr/bin/python3
"""7-base_geometry module

Defines a BaseGeometry class with an area method and
an integer_validator method for validating positive integers.
"""


class BaseGeometry:
    """BaseGeometry class with area() and integer_validator() methods"""

    def area(self):
        """Raise an exception for unimplemented area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer

        Args:
            name (str): name of the variable
            value (any): value to validate

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is <= 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
