"""
Part 1
"""


locations_left = []
locations_right = []

with open("input.txt", 'r') as myfile:
    for line in myfile.readlines():
        locleft, locright = map(int, line.split())
        locations_left.append(locleft)
        locations_right.append(locright)


locations_left.sort()
locations_right.sort()

res = sum((abs(left - right) for left, right in zip(locations_left, locations_right)))


print(res)


"""
Part 2
"""

from collections import Counter

counterleft = Counter(locations_left)
counterright = Counter(locations_right)

sum = 0
for num, repetitions in counterleft.items():
    sum += num * counterright[num] * repetitions

print(sum)
