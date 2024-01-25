#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None:
        return
    for ord_keys in sorted(a_dictionary.keys()):
        print("{}: {}".format(ord_keys, a_dictionary.get(ord_keys)))
