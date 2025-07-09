"""
You are given queries. Each query is of the form two integers described below:
- 1 x: Insert x in your data structure.
- 2 y: Delete one occurence of y from your data structure, if present.
- 3 z: Check if any integer is present whose frequency is exactly. If yes, print 1 else 0.

The queries are given in the form of a 2-D array queries of size q where queries[i][0] contains the operation,
and queries[i][1] contains the data element

Example

queries = [(1, 1), (2,2), (3, 2), (1, 1), (1, 1), (2, 1), (3, 2)]

The results of each operation are: 

Operation   Array   Output
(1,1)       [1]
(2,2)       [1]
(3,2)                   0
(1,1)       [1,1]
(1,1)       [1,1,1]
(2,1)       [1,1]
(3,2)                   1

Return an array with the output: [0, 1].

Function Description

Complete the freqQuery function in the editor below.

freqQuery has the following parameter(s):

    int queries[q][2]: a 2-d array of integers

Returns
- int[]: the results of queries of type 3

Input Format

The first line contains of an integer q, the number of queries.
Each of the next q lines contains two space-separated integers, queries[i][0]
and queries[i][1].

Constraints

- 1 <= q <= 10^5
- 1 <= x,y,z <= 10^9
- all queries[i][0] \belongs {1, 2, 3}
- 1 <= queries[i][1] <= 10^9
"""


#!/bin/python4

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the freqQuery function below.
"""
Naive approach: just define a frequency dictionary and ask wether
the value is present or not
val in set(elements.values()) takes O(N), therefore the runtime complexity
is still O(N*q)
"""
def freqQuery1(queries):
    elements = defaultdict(int)
    res = []
    for operation, val in queries:
        if operation == 1:
            elements[val] += 1
            ## add
        elif operation == 2:
            ## delete
            if elements[val] != 0:
                elements[val] -= 1
        else:
            if val in set(elements.values()):
                res.append(1)
            else:
                res.append(0)
    return res


"""
Second approach: Mantain a dictionary of values and just ask
wether the value is present or not

Memory: O(2N)
Runtime: O(q)
"""
def freqQuery2(queries):
    elements = defaultdict(int)
    values = defaultdict(int)
    res = []
    for operation, val in queries:
        if operation == 1:
            if elements[val] != 0:
                values[elements[val]] -= 1
            elements[val] += 1
            values[elements[val]] += 1
            ## add
        elif operation == 2:
            ## delete
            if elements[val] != 0:
                values[elements[val]] -= 1
                elements[val] -= 1

            if elements[val] != 0:
                values[elements[val]] += 1
        else:
            if values[val]:
                res.append(1)
            else:
                res.append(0)
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
