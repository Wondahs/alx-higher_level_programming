#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a_0 = 0 if (len(tuple_a) < 1) else tuple_a[0]
    a_1 = 0 if (len(tuple_a) < 2) else tuple_a[1]
    b_0 = 0 if (len(tuple_b) < 1) else tuple_b[0]
    b_1 = 0 if (len(tuple_b) < 2) else tuple_b[1]
    result = (a_0 + b_0, a_1 + b_1)
    return (result)
