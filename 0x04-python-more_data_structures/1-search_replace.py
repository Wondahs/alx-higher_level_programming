#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    if (len(my_list) == 0):
        return (new_list)
    for element in my_list:
        if (element == search):
            new_list.append(replace)
            continue
        new_list.append(element)
    return (new_list)

