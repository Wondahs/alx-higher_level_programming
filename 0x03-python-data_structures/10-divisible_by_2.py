#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    truth_list = []
    for index, value in enumerate(my_list):
        truth_list.append(True if value % 2 == 0 else False)
    return (truth_list)
