"""
A balanced partition is a split of an array into two parts (without reordering
any elements) such that the sum of numbers before the split equals the sum of
numbers after the split.

You are given a file containing N arrays of integers, one array per line, where
each array is represented as comma-separated integers.

For each array in the file, if the array can be partitioned in a balanced way,
return the balanced partitions.

Example Input:

# file.txt
1,2,3,4
1,4,5

Expected Output:
[[1,4], [5]]

How big can N get? -> If not too big, brute force and that's it

How big can these arrays per line be? -> If they are super small and
N not to big, brute force

Can i have negative numbers? -> If yes, then is more complicated.
If not, then the prefixsum will be an increasing sequence.

[1, 5, 9]
j = len(n) // 2
possible_middle = prefixsum[j]

if all values are non-negative (Does it work for negative numbers?)
prefixsum[i] = sum(a[:i+1])
prefixsum[j] = sum(a[:j+1])
if j < i => prefixsum[i] - prefixsum[j] = sum(a[j+1:i+1])

What I'm looking for is a k such that sum(a[:k]) = sum(a[k+1:]) =>
sum(a[:k]) - sum(a[k+1:]) = 0


Note: prefixsum[i] - prefixsum[j] => sum(a[]

if possible_middle == prefixsum[n-1] - prefixsum[j]

sum(a[i:]) = sum(a[i] + a[i+1] .. + a[n-1]) = prefixsum[n-1] - prefixsum[i]

"""

from typing import Optional


def run_algorithm(algorithm_to_use):
    res = []
    with open("balanced_partition_input.txt") as inputfile:
        for line in inputfile:
        #for line in inputfile.readlines():  WARNING: This reads the whole ocntent of the file into memory!!!
            array_line = list(map(int, line.split(',')))
            sol_line = algorithm_to_use(array_line)
            if sol_line is not None:
                res.append(sol_line)
    return res


def brute_force(a: list[int]) -> Optional[list[list[int]]]:
    n = len(a)
    if n < 2:
        return None

    for i in range(1, n):
        if sum(a[:i]) == sum(a[i:]):
            return [a[:i], a[i:]]


def balanced_partition(a: list[int]) -> Optional[list[list[int]]]:
    """
    Return balanced partition using prefixsum
    """
    n = len(a)
    prefixsum = [0] * n

    if n < 2:
        # There are no balanced partiitons we can create form this array
        return None

    prefixsum[0] = a[0]
    for i, elem in enumerate(a):
        if i == 0:
            continue
        prefixsum[i] += prefixsum[i-1] + elem

    for i in range(1, n):
        if prefixsum[i] == (prefixsum[n-1] - prefixsum[i]):
            return [a[:i], a[i:]]

    return None



# For small inputs
print(run_algorithm(brute_force))

# For bigger N 
print(run_algorithm(balanced_partition))


"""
Lesson learned: Don't use for line in f.readlines() !! This returns a list of all lines
of the file. Instead, just do this: for line in f: --> This creates a generator over
the file which is way more efficient!

Under the hood:
- When calling line in f: you are calling the __next__ function of the stream (it's an
iterable)
- The method yields 1 line each time (where a line ends up in either \n or \n\r)
- In C: Cpython uses both bufferedio.c (https://github.com/python/cpython/blob/main/Modules/_io/bufferedio.c)
and textio.c(https://github.com/python/cpython/blob/main/Modules/_io/textio.c)
- OS level: Because we call per 8KB of file, we allow the O.S. to be more efficient
and cache other portions of the file
"""


"""
Interesting question:

Is it possible for a row within the file to be larger than fit in memory?

If it is, then the above solution would still work because we are saving
the sum. We would just need to modify a bit the solution such that we
return the sum from a function that iterates over a line which has to
be read as the file (in chunks)

For later returning the final result, instead of returning both partitions
of the array we could just return the index in which we found a balanced partition
"""
