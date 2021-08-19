"""
Determine if the sum of two integers is equal to the given value
Given an array of integers and a value, determine if there are any two integers in the array whose sum is equal to the
 given value. Return true if the sum exists and return false if it does not. Consider this array and the target sums:

[5, 7, 1, 2, 8, 4, 3]
Target 10: 7+3, 2+8
Target 19: No 2 values sum
"""

given = [5, 7, 1, 2, 7, 4, 3]
search = 10

def sum_two_target(given: list, search: int)->bool:
    # determine if there are any two = return early when a single match is found
    # algorithm: add values to a set, then check while searching given list if target - current exists in set
    my_set = set(given)
    for element in given:
        if search - element in my_set:
            return True
    return False

def sum_two_target_naive(given: list, search: int)->bool:
    # determine if there are any two = return early when a single match is found
    # algorithm: check every combination of 2 elements
    for i in range(len(given)): # indexing by int to avoid comparing to self
        for j in range(len(given[i:])):
            i_val = given[i]
            j_val = given[j]
            if i_val + j_val == search:
                return True
    return False

sum_two_target(given, search)
sum_two_target_naive(given, search)
