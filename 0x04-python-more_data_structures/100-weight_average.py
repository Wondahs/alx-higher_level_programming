#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list or not isinstance(my_list, list) or (len(my_list) == 0):
        return (0)
    product = 0
    weight = 0
    average = 0
    for pair in my_list:
        product += pair[0] * pair[1]
        weight += pair[1]
    average = float(product) / weight
    return (average)
