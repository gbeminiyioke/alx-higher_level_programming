#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is None:
        return
    list_cpy = my_list[:]
    for i, elmnt in enumerate(list_cpy):
        if elmnt == search:
            list_cpy[i] = replace
    return list_cpy
