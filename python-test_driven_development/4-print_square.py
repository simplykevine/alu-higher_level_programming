#!/usr/bin/python3
"""A function to sperate words in python"""
'''
File_name: 4-print_square.py
Created: 5-DEC-2023
Author: UMUTONI Kevine (simplykevine)
Size: Large
Project: python-test_driven_development
Status: Not yet submitted.
'''


def print_square(size):
    """Print a square with the # character.

    Args:
        size (int): The height/width of the square.
    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
