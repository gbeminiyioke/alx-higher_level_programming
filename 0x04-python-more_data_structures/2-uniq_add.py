#!/usr/bin/python3

def uniq_add(my_list=[]):
    new_list = set()
    for item in my_list:
        new_list.add(item)
    return sum(new_list)
