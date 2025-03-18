from os import *
from sys import *
from collections import *
from math import *

#a bc # 1 
#def  # 2
#ghij # 1
def wordWrap(words, m, n):
    total_cost = 0
    chars_in_line = 0

    # l = a_, chars_in_line = 2, m = 5, total_count = 0
    # l = a_bc_, chars_in_line = 2 + 3=5, m=5, total_count = 0
    # l = def_, total_cost = 5 - (5 - 1)= 1
    # l = ghij_, total_cost = 1 + (5 - (4 - 1))=1 + 8 = 9

    for word in words:
        curr_len = len(word)
        if chars_in_line + curr_len <= m:
            chars_in_line += curr_len
        else:
            # calculate cost for this line. Remove the extra space added
            total_cost += math.pow(m - (chars_in_line - 1), 3)
            # move to next line
            # according to constraints, a word will always fit in an empty line
            # meaning we can add this word without worrying about m
            chars_in_line = curr_len 
        
        if chars_in_line + 1 <= m: # add space character
            chars_in_line += 1
        else:
            total_cost += math.pow(m - chars_in_line, 3)
            chars_in_line = 0

    if chars_in_line != 0:
        total_cost += math.pow(m - (chars_in_line - 1), 3)
            
    return total_cost



assert 0 == wordWrap(["ab", "a", "b"], 6, 3)

assert 10 == wordWrap(["a", "bc", "def", "ghij"], 5, 4)
