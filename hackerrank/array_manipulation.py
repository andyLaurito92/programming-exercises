"""
Starting with a 1-indexed array of zeros and a list of operations, for each operation add a value to each array element between two given indices, inclusive. Once all operations have been performed, return the maximum value in the array. 

n: number of elements in the array
m: number of queries in the queries array
queries[i] contains (a, b, k) where:

Constraints 

3 <= n <= 10^7
1 <= m <= 2*10^5
1 <= a <= b <= n
0 <= k <= 10^9


Constraint 

"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

# Inefficient but works. O(m * k) where m is the number of queries
# and k is the range of the queries. The worst case scenario is k = n for
# all queries => O(m * n)
def arrayManipulation1(n, queries):
    a = [0] * n
    for query in queries:
        i = query[0] - 1
        j = query[1]
        val = query[2]
        for k in range(i, j):
            a[k] += val
    
    max_val = 0
    for k in range(n):
        if a[k] > max_val:
            max_val = a[k]
    return max_val


"""
Note: This method implements the prefix sum array (which is precalculated list)
"""
def arrayManipulation2(n, queries):
    precalculated = [0] * (n + 2)
    for query in queries:
        a, b, k = query
        precalculated[a] += k
        precalculated[b + 1] += -k # up to here the value k

    max_val = 0
    for i in range(1, n + 1):
        precalculated[i] += precalculated[i - 1]
        if precalculated[i] > max_val:
            max_val = precalculated[i]

    return max_val


def arrayManipulation3(n, queries):
    d = {}
    for query in queries:
        a, b, k = query
        d.setdefault(a, 0)
        d[a] = d[a] + k
        d.setdefault(b+1, 0)
        d[b+1] = d[b+1] - k

    max_val = 0
    curr = 0
    for x in sorted(d):
        curr += d[x]
        if curr > max_val:
            max_val = curr
    return max_val 


def read_input(filename: str) -> (int, list[list[int]]):
    with open('array_manipulation_input.txt') as fd:
        first_line = list(map(int, fd.readline().split(' ')))
        n = first_line[0]
        m = first_line[1]
        queries = []
        for i in range(m):
            query = list(map(int, fd.readline().split(' ')))
            queries.append(query)

    return n, queries


n, queries = read_input('array_manipulation_input.txt')
assert 2484930878 == arrayManipulation2(n, queries)
assert 2484930878 == arrayManipulation3(n, queries)

assert 10 == arrayManipulation1(10, [[1, 5, 3], [4, 8, 7], [6, 9, 1]])
assert 10 == arrayManipulation2(10, [[1, 5, 3], [4, 8, 7], [6, 9, 1]])
assert 10 == arrayManipulation3(10, [[1, 5, 3], [4, 8, 7], [6, 9, 1]])


# 31
assert 31 == arrayManipulation2(10, [[2, 6, 8], [3, 5, 7], [1 ,8 ,1], [5 ,9 ,15]])

assert 882 == arrayManipulation2(4, [[2, 3, 603], [1, 1, 286], [4, 4, 882]])
