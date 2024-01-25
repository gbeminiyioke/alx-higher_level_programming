#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    key_val = {key: value}
    a_dictionary.update(key_val)
    return a_dictionary
