"""
Given two strings, a and b, that may or may not be of the same length, determine the minimum number of character deletions required to make
a and b anagrams. Any characters can be deleted from either of the strings.

Example

a = 'cde'
b = 'dcf'

Delete e from a and f from b so that the remaining strings are cd and dc which
are anagrams. This takes 2 character deletions.

Function Description

Complete the makeAnagram function in the editor below.

makeAnagram has the following parameter(s):

    string a: a string
    string b: another string

Returns

    int: the minimum total characters that must be deleted

Input Format

The first line contains a single string, a

The second line contains a single string, b

Constraints
1 <= |a|, |b| <= 10^4

The strings and consist of lowercase English alphabetic letters, ascii[a-z].

"""


import math
import os
import random
import re
import sys
from string import ascii_lowercase


def makeAnagram(a, b):
    letters = list(ascii_lowercase)
    r = len(letters) # number of letters between a - z
    mapping = { letter: i for i, letter in enumerate(letters) }
    count_letters_a = [0] * r
    count_letters_b = [0] * r
    
    for i in range(len(a)):
        count_letters_a[mapping.get(a[i])] += 1
    
    for i in range(len(b)):
        count_letters_b[mapping.get(b[i])] += 1
        
    to_delete = 0
    for i in range(r):
        to_delete += abs(count_letters_a[i] - count_letters_b[i])
        
    return to_delete


makeAnagram("cde", "dcf")
