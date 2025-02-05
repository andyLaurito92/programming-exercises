"""
You are given an unordered array consisting of consecutive integers

[1, 2, 3, ..., n] without any duplicates. You are allowed to swap any two
elements. Find the minimum number of swaps required to sort the array in
ascending order.

Example

Perform the following steps:

i   arr                         swap (indices)
0   [7, 1, 3, 2, 4, 5, 6]   swap (0,3)
1   [2, 1, 3, 7, 4, 5, 6]   swap (0,1)
2   [1, 2, 3, 7, 4, 5, 6]   swap (3,4)
3   [1, 2, 3, 4, 7, 5, 6]   swap (4,5)
4   [1, 2, 3, 4, 5, 7, 6]   swap (5,6)
5   [1, 2, 3, 4, 5, 6, 7]

It took

swaps to sort the array.

Function Description

Complete the function minimumSwaps in the editor below.

minimumSwaps has the following parameter(s):

    int arr[n]: an unordered array of integers

Returns

    int: the minimum number of swaps to sort the array

Input Format

The first line contains an integer n, the size of arr.
The second line contains space-separated integers arr[i]

Contraints:

1 <= n <= 10^5
1 <= arr[i] <= n

"""

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    num_swaps = 0
    n = len(arr)
    value_to_idx = {arr[i] : i for i in range(n)}
    
    for i in range(n):
        current_min = i + 1 # This is the min value of subarray [i .. n]
        if arr[i] == current_min:
            continue # Min already in its position
        
        min_idx = value_to_idx[current_min] 
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        value_to_idx[arr[min_idx]] = min_idx # We update the element we swapped
        num_swaps += 1
    return num_swaps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
