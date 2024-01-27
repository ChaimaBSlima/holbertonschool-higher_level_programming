#!/usr/bin/python3
def no_c(my_string):
    ch = ""
    for i in my_string:
        if i.upper() != 'C':
            ch += i
    return (ch)
