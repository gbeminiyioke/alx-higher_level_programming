#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        for elements in range(x):
            print("{}".format(my_list[elements]), end='')
            i = i + 1
    except IndexError:
        pass
    print()
    return i
