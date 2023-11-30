#!/usr/bin/python3
def calculate():
    import sys
    from calculator_1 import add, sub, mul, div
    arg = sys.argv
    size = len(sys.argv) - 1
    if size != 3:
        print("Usage: {} <a> <operator> <b>".format(arg[0]))
        sys.exit(1)
    n1 = int(arg[1])
    n2 = int(arg[3])
    op = arg[2]
    if op == '+':
        print("{} {} {} = {}".format(n1, op, n2, add(n1, n2)))
    elif op == '-':
        print("{} {} {} = {}".format(n1, op, n2, sub(n1, n2)))
    elif op == '*':
        print("{} {} {} = {}".format(n1, op, n2, mul(n1, n2)))
    elif op == '/':
        print("{} {} {} = {}".format(n1, op, n2, div(n1, n2)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)


if __name__ == "__main__":
    calculate()
