"""
Generate a minesweeper grid (2x3) with 3 randomly-placed mines

- [0, 3] -> represent how many mines we have adjacent to us
- Total mines = 3
- 2 rows, 3 columns
"""

"""
9 3 1 
9 9 1 

"""


import random


"""
Minesweeper running in O(N^M) with equal probability each cell to be
selected
"""
def minesweeper(n: int = 2, m: int = 3, k: int = 3) -> list[list[int]]:
    board = [[-1] * m for _ in range(n)]
    mine_pos = random.sample([(i, j) for i in range(n) for j in range(m)], k = 3)

    def valid(i: int, j: int) -> bool:
        return 0 <= i and i < n and 0 <= j and j < m

    def neighbors(i: int, j:int) -> list[(int, int)]:
        return [(k, q) for k in range(i-1, i+2) for q in range (j-1, j+2) if valid(k, q)]

    for i, j in mine_pos:
        board[i][j] = 9

    for i in range(n):
        for j in range(m):
            if board[i][j] == 9:
                continue
            count = 0
            for k, q in neighbors(i, j):
                if valid(k, q) and board[k][q] == 9:
                    count += 1
            board[i][j] = count
    return board


minesweeper(2, 3, 3)
