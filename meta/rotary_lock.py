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

# Write any import statements here
def leftDistance(curr:int, to:int, N: int) -> int:
  #1. Distance from curr to N. We know that always there's 1
  # meaning distance from 1 to N is 1
  res = curr - 1 # distance to the beginning
  if to == 1:
    return res
  elif to == N:
    return res + 1
  else:
    res += 1 # Distance from 1 to N
    res += N - to
  return res

def rightDistance(curr:int, to:int, N:int) -> int:
  return abs(curr - to)

def getMinCodeEntryTime(N: int, M: int, C: list[int]) -> int:
  curr = 1  
  res = 0
  memory = {}
  for c in C:
    if memory.get((curr,c)) is not None:
        res += memory.get((curr, c))
    else:
      left = leftDistance(curr, c, N)
      right = rightDistance(curr, c, N)
      if  left < right:
        res += left
        memory[(curr,c)] = left
      else:
        res += right
        memory[(curr,c)] = right
    curr = c
  return res


assert 1 == leftDistance(1, 10, 10)
assert 4 == leftDistance(1, 7, 10)
assert 6 == leftDistance(4, 8, 10)
assert 2 == leftDistance(1, 9, 10)

assert 2 == getMinCodeEntryTime(3, 3, [1, 2, 3])
assert 11 == getMinCodeEntryTime(10, 4, [9, 4, 4, 8])

assert 0 == getMinCodeEntryTime(100, 1, [1])
assert 0 == getMinCodeEntryTime(100, 10, [1] * 10)


"""
Second solution, way simpler using arithmetic module
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
"""
