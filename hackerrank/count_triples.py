# !/bin/python3

import math
import os
import random
import re
import sys


# [1, 3, 9, 9, 27, 81] 
# val = 1, right = {3: 1}
# val = 3, middle = {9: 1}, right = {3: 1, 9: 1}
# val = 9, num_triplets = 1, middle = {9: 1, 81: 1}, right = {3:1, 9:1, 81: 1}
# val = 9, num_triplets = 2, middle = {9: 1, 81: 2}

def countTriplets3(arr, r):
    potential_middle = {}
    potential_right = {}
    num_triplets = 0

    for val in arr:
        # If the current value is the third element of a geometric progression,
        # increment the count of triplets by the number of potential middle elements.
        if val in potential_middle:
            num_triplets += potential_middle[val]

        # If the current value is the second element of a geometric progression,
        # update the potential right elements.
        if val in potential_right:
            potential_middle[val * r] = potential_middle.get(val * r, 0) + potential_right[val]

        # Update the potential right elements for the next iteration.
        potential_right[val * r] = potential_right.get(val * r, 0) + 1

    return num_triplets



def countTriplets1(arr, r):
    """
    Count triplets such that i < j < k and a[i], a[j] = a[i] * r and a[k] = a[j] * r
    Runtime = O(N^3)
    Memory = O(1)
    """

    n = len(arr)
    count = 0

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n ):
                if arr[j] == arr[i] * r and arr[k] == arr[j] * r:
                    count += 1
    return count

def countTriples2(arr, r):
    """
    Count triplets such that i < j < k and a[i], a[j] = a[i] * r and a[k] = a[j] * r
    Runtime = O(N^3)
    Memory = O(1)
    """

    n = len(arr)
    count = 0

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n ):
                if arr[j] == arr[i] * r and arr[k] == arr[j] * r:
                    count += 1
    return count


# 1, 3, 9, 3, 9, 27, r = 3
# val = 27, elements = {}
# val = 9, elements = {27: 1}
# val = 3, elements = {27: 1, 9: 1}, count = 1
# val = 9, elements = {27: 1, 9: 1, 3: 1}, count = 1
# val = 3, elements = {27: 1, 9: 2, 3: 1}, count = 3
# val = 1, elements = {27: 1, 9: 2, 3: 2}, count = 7
def countTripletsbackwards(arr, r):
    n = len(arr)
    count = 0
    elements = {}

    for i in range(n - 1, -1, -1):
        val = arr[i]
        second = val * r
        third = second * r

        repetitions_second = elements.get(second, None)
        repetitions_third = elements.get(third, None)
        if repetitions_second and repetitions_third:
            # number of ways to choose 1 element from repetitions_second
            # * number of ways to choose 1 element from repetitions_third
            count += repetitions_second * repetitions_third

        elements[val] = elements.get(val, 0) + 1

    return count
        

# Complete the countTriplets function below.
def countTriplets(arr, r):
    elements = {}
    for i, elem in enumerate(arr):
        indexes = elements.get(elem, list())
        indexes.append(i)
        elements[elem] = indexes

    if len(elements.keys()) == 1:
        # All elements are equal! We calculate the combinatory number (n 3)
        n = len(arr)
        total = (n * (n-1) * (n-2)) // 6
        return total

    num_triplets = 0
    for i, val in enumerate(arr):
        first = val * r
        second = first * r
        indexes_first = elements.get(first)
        indexes_second = elements.get(second)
        if indexes_first is None or indexes_second is None:
            continue

        # Because how we built it, indexes are sorted!
        # This means that in the moment i >=j, we can
        # stop
        for j in indexes_first:
            if j < i:
                continue
            for k in indexes_second:
                if i < j and j < k:
                    num_triplets += 1
            
    return num_triplets


countTriplets([1] * 100, 1)

def read_input(txtfile: str):
    with open(txtfile) as fp:
        n, r = list(map(int, fp.readline().rstrip().split()))

        elements = list(map(int, fp.readline().rstrip().split()))

    return r, elements


r, arr = read_input('count_triples_input.txt')
countTriplets(arr, r)


assert 6 == countTriplets1([1, 3, 9, 9, 27, 81], 3)
countTripletsbackwards([1, 3, 9, 9, 27, 81], 3)

r, arr = read_input('count_triples_input2.txt')
assert 2325652489 == countTriplets2(arr, r)

assert 2325652489 == countTripletsbackwards(arr, r)
countTripletsbackwards(arr, r)
