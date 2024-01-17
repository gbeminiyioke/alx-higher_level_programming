#!/usr/bin/python3
def to_uper(x):
    if ord(x) >= 97 and ord(x) <= 122:
        return (ord(x) - 32)
    else:
        return ord(x)

def uppercase(str):
    mystring = ""
    for x in str:
        mystring += "%c" % to_uper(x)
    print("{:s}".format(mystring))
