#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = dict()
    if (len(a_dictionary) != 0):
        for key in a_dictionary.keys():
            new_dict[key] = a_dictionary[key] * 2
    return (new_dict)
