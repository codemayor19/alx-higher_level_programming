#!/usr/bin/python3
def calculate():
    import sys
    from calculator_1 import add, sub, mul, div
    arg = sys.argv
    size = len(sys.argv) - 1
    if size != 3:
        print("Usage: {} <a> <operator> <b>".format(arg[0]))
        sys.exit(1)
    elif arg[2] == '+':
        print("{} {} {} = {}".format(arg[1], arg[2], arg[3], add(int(arg[1]), int(arg[3]))))
    elif arg[2] == '-':
        print("{} {} {} = {}".format(arg[1], arg[2], arg[3], sub(int(arg[1]), int(arg[3]))))
    elif arg[2] == '*':
        print("{} {} {} = {}".format(arg[1], arg[2], arg[3], mul(int(arg[1]), int(arg[3]))))
    elif arg[2] == '/':
        print("{} {} {} = {}".format(arg[1], arg[2], arg[3], div(int(arg[1]), int(arg[3]))))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

if __name__ == "__main__":
    calculate()
