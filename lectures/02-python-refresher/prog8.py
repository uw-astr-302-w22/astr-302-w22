#!/usr/bin/env python
#
# Add two numbers passed in on the command line
# But now make it robust.
# And refactor our code to put common elements into a function and avoid duplication.
# Further reduce duplication and show how to use loops
# And make it Pythonic!
# Now make it super pythonic: catch exceptions!
#

import sys

def exit_with_msg(msg):
    """ Prints a usage message and exits the program. """
    print("{}\n\nUsage: {} <arg1> <arg2>".format(msg, sys.argv[0]))
    exit(0)

#### The main program begins here

try:
    a = float(sys.argv[1])
    b = float(sys.argv[2])

    print (a + b)
except IndexError:
    exit_with_msg("Error: two arguments required.")
except ValueError as e:
    exit_with_msg("Error: {}. All arguments must be numbers.".format(e))
