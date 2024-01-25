#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dic_mul_2 = {}
    for item in a_dictionary:
        dic_mul_2[item] = a_dictionary[item] * 2
    return dic_mul_2
