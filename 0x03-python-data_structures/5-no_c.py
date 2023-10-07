#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    for letter in my_string:
        if (ord(letter) != ord("c")) and (ord(letter) != ord("C")):
            new_str += letter
    return (new_str)
