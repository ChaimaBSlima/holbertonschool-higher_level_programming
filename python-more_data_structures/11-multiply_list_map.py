#!/usr/bin/env python3

def multiply_list_map(my_list=[], number=0):
    mapped_list = map(lambda item: item * number, my_list)
    return (list(mapped_list))
