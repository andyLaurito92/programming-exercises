"""
LSD (least significant digit) radix sort is an algorithm that has been around since the 80's :D.
It's based on key-index-counting. The main idea is to use key-index-counting
backwards so we sort an array of strings of FIXED length
"""

from random import choice
from string import ascii_lowercase
from timeit import time

r = len(ascii_lowercase) # number of elements in the alphabet
lowercase_letters = list(ascii_lowercase)
mapping = {letter: i for i, letter in enumerate(lowercase_letters)}

def generate_random_string(size: int) -> str:
    return ''.join([lowercase_letters[(choice(range(r)))] for _ in range(size)])
    

size_strings = 10
mystrings = [generate_random_string(size_strings) for _ in range(10)]
n = len(mystrings)

start = time.time()

aux = [0] * n

for i in reversed(range(n)):
    count = [0] * (r + 1)
    for j in range(n):
        count[mapping.get(mystrings[j][i]) + 1] += 1

    for j in range(r):
        count[j + 1] += count[j]

    for j in range(n):
        aux[count[mapping.get(mystrings[j][i])]] = mystrings[j]
        count[mapping.get(mystrings[j][i])] += 1

    for j in range(n):
        mystrings[j] = aux[j]

    
