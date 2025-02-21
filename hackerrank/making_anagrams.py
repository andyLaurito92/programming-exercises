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
