#!/usr/bin/python3
"""1-my_list module"""

class MyList(list):
    """Custom list class"""

    def print_sorted(self):
        """Print the list sorted in ascending order"""
        print(sorted(self))
