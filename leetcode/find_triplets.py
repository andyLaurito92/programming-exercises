"""
Given a list, find all (i, j, k) such that
i < j < k and a[i] < a[j] < a[k]
"""

def find_triplets(a: list[int]):
    
    n = len(a)
    if n < 3:
        return []

    valid_tuples = []
    for i in range(n):
        for j in range(i, n):
            if i < j and a[i] < a[j]:
                valid_tuples.append((i, j))

    res = []
    for i, j in valid_tuples:
        for k in range(j, n):
            if a[j] < a[k]:
                res.append((i, j, k))

    return res
