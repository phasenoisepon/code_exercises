"""
Determine if the sum of two integers is equal to the given value
Given an array of integers and a value, determine if there are any two integers in the array whose sum is equal to the
 given value. Return true if the sum exists and return false if it does not. Consider this array and the target sums:

[5, 7, 1, 2, 8, 4, 3]
Target 10: 7+3, 2+8
Target 19: No 2 values sum
"""


class ArraySumming:
    @staticmethod
    def sum_two_target(given: list, search: int) -> bool:
        # determine if there are any two = return early when a single match is found
        # algorithm: check if [search - element] exists in the set, then add current value to set
        # avoids comparing to self
        my_set = set()
        for element in given:
            if search - element in my_set:
                return True  # early return
            my_set.add(element)
        return False  # no elements were matched

    @staticmethod
    def sum_two_target_naive(given: list, search: int) -> bool:
        # determine if there are any two = return early when a single match is found
        # algorithm: check every combination of 2 elements
        for i in range(len(given)):  # indexing by int to avoid comparing to self
            for j in range(i + 1, len(given)):
                i_val = given[i]
                j_val = given[j]
                if i_val + j_val == search:
                    return True
        return False


if __name__ == "__main__":
    given = [5, 7, 1, 2, 7, 4, 3]
    search = 10
    result_sum = ArraySumming.sum_two_target(given, search)
    result_naive = ArraySumming.sum_two_target_naive(given, search)

    print("{list} searching for {search} was found {sum}/{naive}".format(list=given, search=search, sum=result_sum,
                                                                         naive=result_naive))
