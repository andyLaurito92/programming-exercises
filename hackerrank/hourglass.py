"""
Given a 6 x 6 2D array, arr, an hourglass is a subset of values with indices falling in the following pattern

There are 16 hourglasses in a 6 x 6 array. The hourglass sum is the sum of the values in an hourglass. Calculate the hourglass sum for every hourglass in arr, then print the maximum hourglass sum.

Constraints:

- 9 <= arr[i][j] <= 9
0 <= i, j <= 5
"""


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def hourglassSum(arr):
    """
    Inefficient but works because the matrix is small (6 x 6).
    What could be improved? -> We are summing several times the
    same intervals of the matrix. Perhaps a prefix sum data
    structure could help us on this

    Additional note: it doesn't, because building that prefix sum
    ds takes at least O(n * m), which is exactly the same runtime we
    currently have
    """
    currmax = None 
    n = len(arr)
    m = len(arr[0])
    for i in range(1, n -1):
        currsum = 0
        for j in range(1, m - 1):
            currsum = arr[i][j] + arr[i-1][j-1] + arr[i -1][j] + arr[i-1][j+1] + arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1]
            if i == 1 and j == 1:
                currmax = currsum # We set as our first max the first value
            elif currsum > currmax:
                currmax = currsum
    return currmax

            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

