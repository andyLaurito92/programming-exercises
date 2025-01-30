""""
There is a string, , of lowercase English letters that is repeated infinitely many times. Given an integer, , find and print the number of letter a's in the first

letters of the infinite string.

Example

The substring we consider is , the first characters of the infinite string. There are

occurrences of a in the substring.

Function Description

Complete the repeatedString function in the editor below.

repeatedString has the following parameter(s):

    s: a string to repeat
    n: the number of characters to consider

Returns

    int: the frequency of a in the substring

Input Format

The first line contains a single string,
.
The second line contains an integer,

.

Constraints:
1 <= |s| <= 100
1 <= n <= 10^12
25% of the test cases, n<= 10^6

"""


#!/bin/python3

import math
import os
import random
import re
import sys
import unittest

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    s_len = len(s)
    count = s.count('a') # count of a's in the string
    if count == 0:
        return 0 # no a's in the string
    
    # how many times does s fit n?
    complete_times_s_fits_in_n = n // s_len
    count *= complete_times_s_fits_in_n
    
    # See how many a's we have for the reminder
    reminder = n % s_len
    count += s[:reminder].count('a')
    
    return count


class TestRepeatedString(unittest.TestCase):
    @classmethod
    def setUp(clss):
        clss.repeatedString = repeatedString

    def test_case1(self):
        self.assertEqual(self.repeatedString('aba', 10), 7)

    def test_case2(self):
        self.assertEqual(self.repeatedString('a', 1000000000000), 1000000000000)
  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
