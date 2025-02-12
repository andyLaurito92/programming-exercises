"""
Harold is a kidnapper who wrote a ransom note, but now he is worried it will be traced back to him through his handwriting. He found a magazine and wants to know if he can cut out whole words from it and use them to create an untraceable replica of his ransom note. The words in his note are case-sensitive and he must use only whole words available in the magazine. He cannot use substrings or concatenation to create the words he needs.

Given the words in the magazine and the words in the ransom note, print Yes if he can replicate his ransom note exactly using whole words from the magazine; otherwise, print No.


Example:

magazine = "attack at dawn"

note = "Attack at dawn"

The magazine has all the right words, but there is a case mismatch. The answer is No. 

checkMagazine has the following parameters:

-string magazine[m]: the words in the magazine
-string note[n]: the words in the ransom note


input format:

The first line contains two space-separated integers, m and n, the numbers of words in the magazine and the note, respectively.
The second line contains m space-separated strings, each magazine[i].
The third line contains n space-separated strings, each note[i]. 

Constraints:

1 <= m, n <= 30000
1 <= legth(magazine[i] & note[i]) <= 5
each word consist of [a-zA-Z]

Sample input:

6 4
give me one grand today night
give one grand today
"""
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

def checkMagazine(magazine, note):
    available_words = Counter(magazine)
        
    for word in note:
        count = available_words.get(word, None)
        if count is None:
            print("No")
            return
        else:
            if count - 1 == 0:
                del available_words[word]
            else: 
                available_words[word] = count - 1
    print("Yes")
        
    # Write your code here

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
