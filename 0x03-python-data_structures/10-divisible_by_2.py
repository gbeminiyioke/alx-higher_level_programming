#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_multiples_of_2 = []
    for num in range(len(my_list)):
        if my_list[num] % 2 != 0:
            list_multiples_of_2.append(False)
        else:
            list_multiples_of_2.append(True)
    return (list_multiples_of_2)
