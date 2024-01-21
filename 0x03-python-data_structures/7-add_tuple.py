#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    len_tuple_a = len(tuple_a)
    len_tuple_b = len(tuple_b)

    if len_tuple_a == 0:
        t_a1 = 0
        t_a2 = 0
    elif len_tuple_a == 1:
        t_a1 = tuple_a[0]
        t_a2 = 0
    else:
        t_a1 = tuple_a[0]
        t_a2 = tuple_a[1]

    if len_tuple_b == 0:
        t_b1 = 0
        t_b2 = 0
    elif len_tuple_b == 1:
        t_b1 = tuple_b[0]
        t_b2 = 0
    else:
        t_b1 = tuple_b[0]
        t_b2 = tuple_b[1]

    tuple_sum = (t_a1 + t_b1, t_a2 + t_b2)
    return(tuple_sum)
