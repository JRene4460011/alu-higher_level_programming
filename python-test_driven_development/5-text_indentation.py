#!/usr/bin/python3
"""Module that contains a function to print text with indentation."""


def text_indentation(text):
    """Prints text with 2 new lines after '.', '?', and ':'.

    Args:
        text (str): text to print

    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    end_chars = ".?:"
    i = 0
    length = len(text)

    while i < length:
        line = ""
        while i < length and text[i] not in end_chars:
            line += text[i]
            i += 1
        if i < length and text[i] in end_chars:
            line += text[i]
            i += 1
        print(line.strip())
        if i < length:
            print("")
