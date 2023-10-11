#!/usr/bin/python3
def uniq_add(my_list=[]):
    added = []
    total = 0
    for num in my_list:
        if (num not in added):
            total += num
            added.append(num)
    return (total)
