#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    first_value = list(a_dictionary.items())[0][1]
    first_key = list(a_dictionary.items())[0][0]

    for key, value in a_dictionary.items():
        if value > first_value:
            first_value = value
            first_key = key

    return first_key
