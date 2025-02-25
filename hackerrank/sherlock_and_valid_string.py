"""
Sherlock considers a string to be valid if all characters of the string appear
the same number of times. It is also valid if he can remove just 1 character at 1
index in the string, and the remaining characters will occur the same number of
times. Given a string s, determine if it is valid. If so, return YES, otherwise
return NO.

Constraints:

- 1 <= |s| <= 10^5
- each character s[i] belongs to ascii[a-z]
"""

#!/bin/python3

import math
import os
import random
import re
import sys
from string import ascii_lowercase

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

# abcdefghhgfedecba
# mapping = {'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 3, 'f': 2, 'g': 2, 'h': 2}
# num_diff_frequencies = [1, 2]
# sorted_count = [1, 2, 2]
# n = 8

def isValid(s):
    def all_equal(a: list[int]) -> bool:
        for i in range(1, len(a)):
            if a[i] != a[i-1]:
                return False
        return True

    mapping = {}
    for letter in s:
        if mapping.get(letter, None) is None:
            mapping[letter] = 1
        else:
            mapping[letter] += 1
        
    num_diff_frequencies = len(set(mapping.values()))
    if num_diff_frequencies == 1:
        # All characters appear the same number of times
        return 'YES'
    elif num_diff_frequencies > 2:
        # I have at least 3 letters with different num of frequencies
        # therefore I cannot substract just 1 of them and have 3 
        # equal elements
        return 'NO'
    else:
        # num_diff_frequencies == 2
        # Only way for this to work is:
        # 1) if all frequencies count equal K and the only different number is K + 1
        # 2) if all frequencies count are K and the smallest frequency is 1 => we can remove
        # the only different value !
        sorted_count = sorted(mapping.values())
        n = len(sorted_count)
        if sorted_count[0] == 1 and all_equal(sorted_count[1:n]):
            return 'YES' # We delete this first char
        elif sorted_count[0] == sorted_count[n - 1] - 1 and all_equal(sorted_count[0:n-1]):
            return 'YES'
        else:
            return 'NO'           


assert 'YES' == isValid("abc")

assert 'NO' == isValid("abccc")

assert 'YES' == isValid("abcdefghhgfedecba")

assert 'YES' == isValid("aabbc")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
