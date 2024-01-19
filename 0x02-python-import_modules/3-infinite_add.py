#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    add_result = 0
    for arg in sys.argv:
        if arg != sys.argv[0]:
            add_result += int(arg)
    print(add_result)
