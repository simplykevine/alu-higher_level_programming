#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    total_score = 0
    num_of_val = 0
    for score, weight in my_list:
        total_score += (score * weight)
        num_of_val += weight
    return total_score / num_of_val
