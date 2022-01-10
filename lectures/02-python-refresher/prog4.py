#!/usr/bin/env python

import sys
import re

isNumber = r'^[1-9][0-9]*\.?[0-9]*([Ee][+-]?[0-9]+)?$';

if len(sys.argv) != 3:
    print("Error: two arguments required.")
    print("")
    print("Usage: {} <arg1> <arg2>".format(sys.argv[0]))
    exit(0)

if not re.search(isNumber, sys.argv[1]):
    print("Error: the first argument must be a number")
    print("")
    print("Usage: {} <arg1> <arg2>".format(sys.argv[0]))
    exit(0)

if not re.search(isNumber, sys.argv[2]):
    print("Error: the second argument must be a number")
    print("")
    print("Usage: {} <arg1> <arg2>".format(sys.argv[0]))
    exit(0)

a = float(sys.argv[1])
b = float(sys.argv[2])

print (a + b)
