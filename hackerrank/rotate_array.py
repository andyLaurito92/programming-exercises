#!/bin/python3

from unittest import TestCase
import math
import os
import random
import re
import sys

#
# Complete the 'rotLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER d
#

def rotLeft(a, d):
    n = len(a)
    d = d % n # we start repeating ourselves otherwise
    rotated_array = [0] * n
    for i in range(n):
        rotated_array[i - d] = a[i]

    for i in range(n):
        a[i] = rotated_array[i]
       
    return a
   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()


class SolutionTests(TestCase):

    def test_case1(self):
        nums = [1, 2, 3, 4, 5, 6, 7]
        k = 3

        rotLeft(nums, k)

        self.assertEqual([4, 5, 6, 7, 1, 2, 3], nums, "Rotate 1 didn't get expected result")

    def test_case2(self):
        nums = [-1, -2, 99, 100]
        k = 2

        rotLeft(nums, k)

        self.assertEqual([99, 100, -1, -2], nums, "Rotate 1 didn't get expected result")

    def test_case3(self):
        nums = [1,2,3,4,5,6]
        k = 3

        rotLeft(nums, k)

        self.assertEqual([4, 5, 6, 1, 2, 3], nums, "Rotate 1 didn't get expected result")

from pprint import pprint
stream = StringIO()
runner = unittest.TextTestRunner(stream=stream)
result = runner.run(unittest.makeSuite(SolutionTests))
print("tests run ", result.testsRun)
print("Errors ", result.errors)
pprint(result.failures)
stream.seek(0)
print("test output\n", stream.read())

