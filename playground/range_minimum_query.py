"""
A range minimum query (RMQ) solves the problem of finding the minimal value in a sub-array of an array of comparable objects.
"""

def rangeminimumquery(a:list[int], queries: list[tuple[int, int]]) -> list[int]:
    """
    Given an array a and a list of queries containing indices such as 0 <= i <= j <= n - 1,
    return a list that contains in each subinterval the minimum value in the subarray a[i, j]
    """

    n = len(a)
    if n == 0:
        return []
    premin = [None] * n
    premin[0] = a[0]
    for i in range(1, n):
        x = a[i]
        if premin[i - 1] < x:
            premin[i] = premin[i - 1]
        else:
            premin[i] = x

    res = [0] * len(queries)
    for k, query in enumerate(queries):
        i, j = query
        res[k] = premin[j]

    return res


    # Idea: To fin the minimum 
    # a = [3, -4, 8, 0, -10, 3]
    # a = [7, 6, 5, 4, 3, 2, 1]
    # premin = [3, -4, -4, -4, -10, -10]
    # premin = [7, 6, 5, 4, 3, 2, 1]


assert [-4, -10, -10] == rangeminimumquery([3, -4, 8, 0, -10, 3], [(0, 3), (1, 4), (2, 4)])


assert [5, 1, 1] == rangeminimumquery([7, 6, 5, 4, 3, 2, 1], [(0, 2), (3, 6), (0, 6)])

assert [-10, -3, 3] == rangeminimumquery([-10, -3, 3, 3, 3, 3], [(0, 3), (1, 3), (2, 4)])
