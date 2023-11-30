#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg = sys.argv
    size = len(sys.argv) - 1
    n = 0
    for i in range(1, size + 1):
        n += int(arg[i])
    print("{}".format(n))
