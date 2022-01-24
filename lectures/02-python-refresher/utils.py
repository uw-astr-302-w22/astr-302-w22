""" A module with useful functions """

def to_floats(lst):
    """ Returns a list of strings corresponding to a list of floats """
    return [ float(arg) for arg in lst ]

def prod(lst):
    """ Computes and returns the product of a list """
    res = 1.
    for x in lst: res *= x
    return res
