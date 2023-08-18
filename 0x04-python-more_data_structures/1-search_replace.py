#!/usr/bin/python3
def replace_elements(my_list, search, replace):
    result = []
    for i in my_list:
        if i == search:
            result.append(replace)
        else:
            result.append(i)
    return result

