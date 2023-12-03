#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    _blist = my_list[:]
    for count, i in enumerate(my_list):
        if i % 2 == 0:
            _blist[count] = True
        else:
            _blist[count] = False
    return (_blist)
