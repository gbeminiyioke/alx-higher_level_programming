#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    div_by = 0
    w_avg = 0
    for tpl in my_list:
        w_avg += tpl[0] * tpl[1]
        div_by += tpl[1]
    return float(w_avg / div_by)
