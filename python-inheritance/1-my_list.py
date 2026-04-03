#!/usr/bin/python3
"""1-my_list module"""


class MyList(list):
    """My custom list class that adds a print_sorted method."""

    def print_sorted(self):
        """Prints the list in ascending order without modifying the original list."""
        print(sorted(self))
