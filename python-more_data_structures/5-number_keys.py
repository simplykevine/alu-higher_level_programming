#!/usr/bin/python3
def number_keys(a_dictionary):
    sum_keys = 0
    for key, value in a_dictionary.items():
        sum_keys += 1

    return int(sum_keys)
