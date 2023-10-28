#!/usr/bin/python3
"""Module that indents text"""


def text_indentation(text):
    """Functiom that indents text.

    Args:
        text (str): Text to indent

    Raises:
        TypeError: if text is not a string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == " ":
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] in ".?:":
            print()
            c += 1

            while c < len(text) and text[c] == " ":
                c += 1
            continue
        c += 1
