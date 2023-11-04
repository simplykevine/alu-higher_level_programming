#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """ deletes the item at a specific position given in a list provided."""
    if idx >= 0 and idx < len(my_list):
        del my_list[idx]
    return my_list
