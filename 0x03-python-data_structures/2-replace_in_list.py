#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    new_list = my_list
    if idx < 0:
        return my_list
    elif idx > len(my_list) - 1:
        return my_list
    else:
        for i in range(0, len(my_list)):
            if i == idx:
                my_list[i] = element
        return new_list
