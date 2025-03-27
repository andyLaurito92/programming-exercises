"""
There's a stack of N inflatable discs, with the ith disc from the top having an
initial radius of Ri​ inches.

The stack is considered unstable if it includes at least one disc whose radius
is larger than or equal to that of the disc directly under it. In other words,
for the stack to be stable, each disc must have a strictly smaller radius than
that of the disc directly under it.

As long as the stack is unstable, you can repeatedly choose any disc of your
choice and deflate it down to have a radius of your choice which is strictly
smaller than the disc’s prior radius. The new radius must be a positive integer
number of inches.

Determine the minimum number of discs which need to be deflated in order to
make the stack stable, if this is possible at all. If it is impossible to
stabilize the stack, return −1 instead.
Constraints
1≤N≤50
1≤Ri≤1,000,000,000

"""

from typing import List
# Write any import statements here

def getMinimumDeflatedDiscCount(N: int, R: List[int]) -> int:
  # Write your code here
  res = 0
  # 2 5 3 6 5, N = 5
  # i = 4, R[4] = 5 < R[3] = 6: R[3] = R[4]-1 = 4, res =1
  # i = 3, R[3] = 4 < R[2] = 3 X
  # i = 2, R[2] = 3 < R[1] = 5 Y: R[1] = R[2] - 1 = 2, res=2
  # i = 1, R[1] = 2 <= R[0] = 2 Y: R[1] = R[2] - 1 = 2, res=2
  for i in reversed(range(1, N)):
    if R[i] <= R[i-1]:
      R[i-1] = R[i] - 1
      res += 1
      if R[i-1] < 1:
        return -1 # Not possible
  return res


assert 3 == getMinimumDeflatedDiscCount(5, [2, 5, 3, 6, 5])

assert 2 == getMinimumDeflatedDiscCount(3, [100, 100, 100])

assert -1 == getMinimumDeflatedDiscCount(4, [6, 5, 4, 3])
