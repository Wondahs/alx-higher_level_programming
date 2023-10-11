#!/usr/bin/python3
def best_score(a_dictionary):
    if (a_dictionary is None or len(a_dictionary) == 0):
        return (None)
    value = -float("inf")
    item = ""
    for key in a_dictionary.keys():
        if (a_dictionary[key] > value):
            value = a_dictionary[key]
            item = key
    return (item)
