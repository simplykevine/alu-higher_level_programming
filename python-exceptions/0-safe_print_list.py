#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num_returned = 0
    for i in range(x):
        try:
            print(f"{my_list[i]}", end="")
            num_returned += 1
        except IndexError as IE:
            break
    print()
    return num_returned
