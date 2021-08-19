import random

"""
You are given an array of positive numbers from 1 to n, such that all numbers from 1 to n are present except one number ‘x’. You have to find ‘x’. The input array is not sorted.
"""
def sum_1_n(n: int) -> int:
    assert n>=1
    return n*(n+1)/2

def find_missing(search: list, n: int) -> int:
    assert len(search)>=2
    assert n>1

    total = sum(search)
    return int(sum_1_n(n) - total)


if __name__ == "__main__":
    length = random.randint(2, 20)
    my_list = list(range(1, length))

    n = length - 1
    #print(my_list)
    #print("List is {length} long and is from 1 to {n}".format(length=length-1, n=n))
    random.shuffle(my_list)
    my_list.pop() # pop the last

    print("List is {length} long and is from 1 to {n}".format(length=len(my_list), n=n))
    print(my_list)
    print(find_missing(my_list, n))

    #python solution
    diff = set(range(1,length)) - set(my_list)
    print("Set diff is {}".format(diff))
