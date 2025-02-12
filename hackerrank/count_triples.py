# !/bin/python3

import math
import os
import random
import re
import sys

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

r, arr = read_input('count_triples_input2.txt')
