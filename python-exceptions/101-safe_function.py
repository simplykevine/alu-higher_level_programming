#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        output = fct(*args)
    except Exception as E:
        print("Exception: {}".format(E), file=sys.stderr)
        return None
    else:
        return output
