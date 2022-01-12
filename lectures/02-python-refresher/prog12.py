#!/usr/bin/env python

import sys
import utils

def exit_with_msg(msg):
    """ Prints a usage message and exits the program. """
    print("{}\n\nUsage: {} [arg1] [arg2] [...]".format(msg, sys.argv[0]))
    exit(0)

#### The main program begins here

try:
    float_list = utils.to_floats( sys.argv[1:] )
    print ( utils.prod( float_list ) )
except ValueError as e:
    exit_with_msg("Error: {}. All arguments must be numbers.".format(e))
