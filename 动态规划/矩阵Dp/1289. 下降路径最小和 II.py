from typing import List


class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(1, m):
            for j in range(n):
                grid[i][j] += min(grid[i - 1][:j] + grid[i - 1][j + 1:])
        return min(grid[-1])

obj = Solution()
print(obj.minFallingPathSum(grid = [[1,2,3],[4,5,6],[7,8,9]]))