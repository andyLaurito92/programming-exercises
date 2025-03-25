"""
A range minimum query (RMQ) solves the problem of finding the minimal value in a sub-array of an array of comparable objects.
"""

def rangeminimumquery(a:list[int], queries: list[tuple[int, int]]) -> list[int]:
    """
    Given an array a and a list of queries containing indices such as 0 <= i <= j <= n - 1,
    return a list that contains in each subinterval the minimum value in the subarray a[i, j]

    NOTE: This doesn't work because it works with prefixes, while the rangeminimumquery
    problem in reallity works with substrings (Pair i, j such that a[i:j])
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



"""
In this approach we will use dp to solve the problem. Let's think on what we want to do:
Subproblem: substrings a[i:j]
Topological order: Iterate over subarrays of length 2 to N
Relation: 
s(a[i:j]) -> We have the minimum value between a[i:j], we want to calculate
the next minimum value
s(a[i:j]) = if s(a[i:j]) > a[j+1] => s(a[i:j+1]) = a[j+1] else s(a[i:j])
s(a[i-1:j] = if s(a[i:j]) > a[i-1] => s(a[i-1:j]) = a[i-1] else s(a[i:j])

Base case: s(a[i:i]) = a[i]
Original problem: s(a[0:n])
Time: O(N^2) because we have N^2 subproblems (substrings) * comparisson per each subproblem which is O(1)
"""
def rangeminimumquery2(a:list[int], queries: list[tuple[int, int]]) -> list[int]:
    n = len(a)

    if len(queries) == 0:
        return []

    if n == 0:
        return []
    elif n == 1:
        return a[0]

    memory = [[None] * (n-i+1) for i in range(n)]
    for i in range(n):
        memory[i][1] = a[i]
        

    for length in range(2, n+1): # The lengths of the subarrays we want to loop over
        for i in range(n - length + 1): # how many subarrays of length length do I have
            j = i + length - 1
            if a[j] < memory[i][length-1]:
                memory[i][length] = a[j]
            else:
                memory[i][length] = memory[i][length-1]

    res = []
    for i, j in queries:
        res.append(memory[i][j-i+1])

    return res


# n = 3, memory = [[None, None, None, None], [None, None, None], [None, None]]
# memory=[[None, 1, 1, None], [None, 2, 2], [None, 3]]
# length in range(2, 4) -> 2, 3
# length=2, i in range(3 - 2 + 1) = range(2) -> 0, 1
# length=2, i=0, j = 0 + 2-1=1
# if 2=a[1] < memory[0][1]=1 X, then memory[0][1] =memory[0][0]=1 
# i = 1, length=2, j = 1 + 2-1=2
# if a[2] < memory[1][1] X = memory[1][2] = 2
# length=3, i in range(3-3+1=1) => i in range(1)
# length=3, i=0, j=0+3-1=2, a[2] < memory[0][2]
assert [1] == rangeminimumquery2([1, 2, 3], [(0, 2)])


assert [-4, -10, -10] == rangeminimumquery2([3, -4, 8, 0, -10, 3], [(0, 3), (1, 4), (2, 4)])
assert [5, 1, 1] == rangeminimumquery2([7, 6, 5, 4, 3, 2, 1], [(0, 2), (3, 6), (0, 6)])
assert [-10, -3, 3] == rangeminimumquery2([-10, -3, 3, 3, 3, 3], [(0, 3), (1, 3), (2, 4)])
