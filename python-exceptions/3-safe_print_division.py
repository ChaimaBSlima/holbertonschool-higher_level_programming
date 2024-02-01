#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        chaima = a / b
    except Exception as e:
        chaima = None
    finally:
        print("Inside result: {}".format(chaima))
    return (chaima)
