#!/usr/bin/python3

"""Defining text_indentation."""


def text_indentation(text):
    """Prints a text with 2 new lines

    Args:
        text: (str)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    indented_t = ""
    punct = ['.', '?', ':']
    for c in text:
        indented_t += c
        if c in punct:
            indented_t += '\n\n'

    print(indented_t.rstrip())
