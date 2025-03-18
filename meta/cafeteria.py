"""
A cafeteria table consists of a row of N seats, numbered from 1 to N from left to right.
Social distancing guidelines require that every diner be seated such that K seats to their
left and K seats to their right (or all the remaining seats to that side if there are fewer
than K) remain empty.

There are currently M diners seated at the table, the ith of whom is in seat Si​.
No two diners are sitting in the same seat, and the social distancing guidelines are satisfied.
Determine the maximum number of additional diners who can potentially sit at the table without
social distancing guidelines being violated for any new or existing diners, assuming that the
existing diners cannot move and that the additional diners will cooperate to maximize how many of them can sit down.
Please take care to write a solution which runs within the time limit.

Constraints
1≤N≤10^15
1≤K≤N
1≤M≤500,000
M≤N
1≤Si≤N
"""


# The trick here is to iterate over S which is the smallest list
def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: list[int]) -> int:
    res = 0
    left = 1
    S.sort()
    for s in S:
        right = s - (K + 1)
        res += 1 + (right - left) // (K + 1)
        left = s + (K + 1)
    res += 1 + (N - left) // (K+1)
        
    return res


# k = 1
# right = 2 - (1 + 1) = 0, left = 1
# res = 1 + (right - left) // (2) = 0
# left = 2 + 1 + 1 = 4
# right = 6 - (1 + 1) = 4, res = 1 + (4 - 4) // 2 = 1
# left = 6 + (2) = 8
# res = 1 + 
assert 3 == getMaxAdditionalDinersCount(10, 1, 2, [2, 6]) 
assert 1 == getMaxAdditionalDinersCount(15, 2, 3, [11, 6, 14])

# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
# - - - - - X - - - -  X -  -  X   -
