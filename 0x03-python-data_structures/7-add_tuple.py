#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    lt_a = list(tuple_a)
    lt_b = list(tuple_b)
    new_list = []
    while len(lt_a) < 2:
        lt_a.append(0)
    while len(lt_b) < 2:
        lt_b.append(0)
    for i in range(2):
        new_list.append(lt_a[i] + lt_b[i])
    return (tuple(new_list))
