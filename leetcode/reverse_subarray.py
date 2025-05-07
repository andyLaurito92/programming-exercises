"""
Given 2 indexes and an array, reverse the order of the elements
in that subarray
"""

def reverse_sublist(a: list, i:int, j:int) -> list:
    if (i < 0 or j < 0) or (i > j):
        raise ValueError("Invalid indexes provided ", i, j)

    for k in range(j - i):
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

test_cases = [
    (([1, 2, 3, 4, 5, 6], 2, 4), [1, 2, 5, 4, 3, 6]),
    (([1, 2, 3, 4, 5, 6], 0, 0), [1, 2, 3, 4, 5, 6]),
    (([1, 2, 3], 0, 2), [3, 2, 1])
]

for test_case, expected in test_cases:
    a, i, j = test_case
    reverse_sublist(a, i, j)
    assert (expected == a), f"Didn't pass. Test case: {a}, {i}, {j}, {expected}"
