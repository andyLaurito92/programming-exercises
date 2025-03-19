"""
You're trying to open a lock. The lock comes with a wheel which has the integers
from 11 to NN arranged in a circle in order around it (with integers 1 and N
adjacent to one another). The wheel is initially pointing at 1.

It takes 1 second to rotate the wheel by 1 unit to an adjacent integer in
either direction, and it takes no time to select an integer once the wheel is
pointing at it.
The lock will open if you enter a certain code. The code consists of a sequence
of M integers, the ith of which is Ci​. Determine the minimum number of seconds
required to select all M of the code's integers in order.

Please take care to write a solution which runs within the time limit.

Constraints
3≤N≤50,000,000
1≤M≤1,000
1≤Ci≤N

"""

def getMinCodeEntryTime2(N: int, M: int, C: list[int]) -> int:
  curr = 1
  res = 0
  for c in C:
    res += min((c-curr) % N, (curr-c)%N)
    curr = c
  return res


assert 2 == getMinCodeEntryTime2(3, 3, [1, 2, 3])
assert 11 == getMinCodeEntryTime2(10, 4, [9, 4, 4, 8])

assert 0 == getMinCodeEntryTime2(100, 1, [1])
assert 0 == getMinCodeEntryTime2(100, 10, [1] * 10)



"""
To review: How modulus work with negative numbers

Concept: wrap-around -> making something linear to behave
as circular by connecting the last element to the first one
"""
