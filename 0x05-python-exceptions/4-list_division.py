#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    list_elements = []
    for list_item in range(list_length):
        try:
            c = my_list_1[list_item] / my_list_2[list_item]
        except IndexError:
            print("out of range")
            c = 0
        except ZeroDivisionError:
            print("division by 0")
            c = 0
        except TypeError:
            print("wrong type")
            c = 0
        finally:
            list_elements.append(c)
    return list_elements
