#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as clc
    from sys import argv
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif argv[2] not in ['+', '-', '*', '/']:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        if argv[2] == '+':
            print("{} + {} = {}".format(a, b, clc.add(a, b)))
            exit(0)
        elif argv[2] == '-':
            print("{} - {} = {}".format(a, b, clc.sub(a, b)))
            exit(0)
        elif argv[2] == '*':
            print("{} * {} = {}".format(a, b, clc.mul(a, b)))
            exit(0)
        elif argv[2] == '/':
            if b != 0:
                print("{} / {} = {}".format(a, b, clc.div(a, b)))
                exit(0)
            else:
                exit(1)
