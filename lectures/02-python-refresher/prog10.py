#!/usr/bin/env python

import sys

def exit_with_msg(msg):
    """ Prints a usage message and exits the program. """
    print("{}\n\nUsage: {} [arg1] [arg2] [...]".format(msg, sys.argv[0]))
    exit(0)

def to_floats(lst):
    """ Returns a list of strings corresponding to a list of floats """
    vals = []
    for arg in lst:
        vals.append( float(arg) )
    return vals

def prod(lst):
    """ Computes and returns the product of a list """
    res = 1.
    for x in lst: res *= x
    return res

#### The main program begins here

try:
    float_list = to_floats( sys.argv[1:] )
    product = prod( float_list )
    print(product)
except ValueError as e:
    exit_with_msg("Error: {}. All arguments must be numbers.".format(e))
