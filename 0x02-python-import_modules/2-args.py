#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg = sys.argv
    l_size = len(arg) - 1
    if l_size > 1:
        print("{} arguments:".format(l_size))
        for x in range(1, l_size + 1):
            print("{}: {}".format(x, arg[x]))
    elif l_size == 0:
        print("{} arguments:".format(l_size))
    else:
        print("{} arguments:".format(l_size))
        print("{} {}".format(l_size, arg[1]))
