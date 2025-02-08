"""
Sorted merge: You are given two sorted arrays, A and B, where A has a large
enough buffer at the end to hold B. Write a method to merge B into A in
sorted order
"""

from random import choice


def sorted_merge(a: list[int], num_elements_a: int, b: list[int]):
    helper = []
    m = len(b)
    for i in range(num_elements_a):
        helper.append(a[i])

    for i in range(m):
        helper.append(b[i])

    i = 0
    j = num_elements_a
    for k in range(num_elements_a + m):
        if i == num_elements_a:
            a[k] = helper[j]
            j += 1
        elif j == num_elements_a + m:
            a[k] = helper[i]
            i += 1
        elif helper[i] > helper[j]:
            a[k] = helper[j]
            j += 1
        else:
            a[k] = helper[i]
            i += 1


size = 3
a = [choice(range(10)) for _ in range(size)]
b = [choice(range(10)) for _ in range(size)]


a.sort()
b.sort()

a.extend([None] * 3)
print(a, b)
sorted_merge(a, size, b)
