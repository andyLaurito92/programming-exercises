"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 300
    grid[i][j] is '0' or '1'.

"""
class UnionFind:
    def __init__(self, n: int):
        self._union = [i for i in range(n)]
        self.count = n

    def union(self, i: int, j: int) -> None:
        "unions group of i w/group of j"
        cci = self.find(i)
        ccj = self.find(j)
        if cci == ccj:
            return
        
        self.count -= 1
        self._union[cci] = ccj

    def find(self, i: int) -> int:
        "Return the connected component id of this element"
        while i != self._union[i]:
            i = self._union[i]
        return i


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        uf = UnionFind(m*n)

        def ufpos(i:int, j:int) -> int:
            return i * n + j

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    # union w/adjacent islands
                    if i-1 >= 0 and grid[i-1][j] == "1":
                        uf.union(ufpos(i-1,j),ufpos(i,j))
                    if i+1 < m and grid[i+1][j] == "1":
                        uf.union(ufpos(i+1,j),ufpos(i,j))
                    if j-1 >= 0 and grid[i][j-1] == "1":
                        uf.union(ufpos(i,j-1),ufpos(i,j))
                    if j+1 < n and grid[i][j+1] == "1":
                        uf.union(ufpos(i,j+1),ufpos(i,j))
                else:
                    uf.count -= 1 # water doesn't count
                    uf._union[ufpos(i,j)] = -1

        return uf.count


sol = Solution()
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  #["1","1","0","0","0"],
  #["0","0","0","0","0"]
]
assert 1 == sol.numIslands(grid)

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
assert 3 == sol.numIslands(grid)
