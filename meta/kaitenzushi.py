"""
There are N dishes in a row on a kaiten belt, with the ith dish being
of type Di​. Some dishes may be of the same type as one another.

You're very hungry, but you'd also like to keep things interesting.
The N dishes will arrive in front of you, one after another in order,
and for each one you'll eat it as long as it isn't the same type as
any of the previous K dishes you've eaten.
You eat very fast, so you can consume a dish before the next one gets to you.
Any dishes you choose not to eat as they pass will be eaten by others.
Determine how many dishes you'll end up eating.
Please take care to write a solution which runs within the time limit.

Constraints

1≤N≤500,00
1≤K≤N
1≤Di≤1,000,000
"""

from collections import deque

def getMaximumEatenDishCount(N: int, D: list[int], K: int) -> int:
  last_k = deque()
  dishes = {}
  res = 0
  for dish in D:
    if dishes.get(dish) is None:
      res += 1
      dishes[dish] = 1
      last_k.appendleft(dish)
      if len(last_k) > K:
        removed = last_k.pop()
        del dishes[removed]
  return res


assert 5 == getMaximumEatenDishCount(6, [1, 2, 3, 3, 2, 1], 1)

assert 4 == getMaximumEatenDishCount(6, [1, 2, 3, 3, 2, 1], 2)

assert 2 == getMaximumEatenDishCount(7, [1, 2, 1, 2, 1, 2, 1], 2)


"""
Important lesson learned from this exercise:

Doing

a = []
a.insert(0, "hey")

Takes O(N) because insert 0 SHIFTS all elements 1 position to the right. Meaning that using a list as a queue it's something SUPER INEFFICIENT

Instead, you need to use dequeue that has amortized O(1) for doing appends (both left and right) and removals

Dequeue is implemented by using double-linked lists

"""
