"""
You are given an n x n 2D matrix representing an image, rotate the image by 90
degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input
2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Constraints:

    n == matrix.length == matrix[i].length
    1 <= n <= 20
    -1000 <= matrix[i][j] <= 1000

"""

def rotate(matrix: list[list[int]]) -> None:
    n = len(matrix)

    new_matrix = [[0] * n for _ in range(n)]
    k = n - 1 
    for i in range(n):
        row_i = matrix[i]
        for j in range(n):
            new_matrix[j][k] = row_i[j]
        k -=1

    for i in range(n):
        for j in range(n):
            matrix[i][j] = new_matrix[i][j]


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotate(matrix)
assert matrix == [[7,4,1], [8,5,2], [9,6,3]]
