# find al positive integer solutions under 1,000 to a^3a + b^3 =c^3 + d^3

# a * a * a + b * b * b = c * c * c + d * d * d

# a * a * a  = c * c * c + d * d * d - b * b * b

import math

# brute force
res = []
# for a in range(1001):
#     for b in range(1001):
#         for c in range(1001):
#             for d in range(1001):
#                 if math.pow(a, 3) + math.pow(b, 3) == math.pow(c, 3) + math.pow(d, 3):
#                     res.append((a, b, c, d))


# A + B = C + D => A = C + D - B

# C = A + B - D
# D = A + B - C


# C = A + B - D
# B = C + D - A

# 

# Optimization
# The trick here is to understand that N^4 is worst than N^2 when N = 1000 :)
# The first ends in 27 days while the second ends in a couple of seconds

# [1, 2, 3, 4, 5] k = 5, s=0, e=5, m=2
def binary_search(mylist, k):
    start = 0
    end = len(mylist) - 1
    while start <= end:
        medium = start + math.floor((end - start) / 2)
        if mylist[medium][0] == k:
            return mylist[medium]
        elif mylist[medium][0] < k:
            start = medium + 1
        else:
            end = medium - 1
    return False


times3_integers_under_1000 = [int(math.pow(i, 3)) for i in range(1001)]
times3_all_sums_under_1000 = []

for a in times3_integers_under_1000:
    for b in times3_integers_under_1000:
        times3_all_sums_under_1000.append((a + b, a, b))


for a in times3_integers_under_1000:
    for b in times3_integers_under_1000:
        k = binary_search(times3_all_sums_under_1000, a + b)
        if k:
            res.append((a, b, k[1], k[2]))
