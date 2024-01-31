#!/usr/bin/python3
def search_replace(my_list, search, replace):
    List = []
    for i in my_list:
        if i == search:
            i = replace
        List.append(i)
    return (List)
