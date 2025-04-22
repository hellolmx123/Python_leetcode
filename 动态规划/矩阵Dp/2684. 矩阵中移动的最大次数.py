from typing import List


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            grid[i].append(0)
        grid.append([0] * len(grid[0]))
        def dfs(i, j):
            if j == len(grid[0]) - 1:
                return 0
            if i >= 1:
                ans1 = dfs(i - 1,j + 1) + 1 if grid[i - 1][j + 1] > grid[i][j] else 0
            else:
                ans1 = 0
            ans2 = dfs(i,j + 1) + 1 if grid[i][j + 1] > grid[i][j] else 0
            if i <= len(grid) - 1:
                ans3 = dfs(i + 1,j + 1) + 1 if grid[i + 1][j + 1] > grid[i][j] else 0
            else:
                ans3 = 0
            return max(ans1,ans2,ans3)
        return max(dfs(n, 0) for n in range(len(grid) - 1))

obj = Solution()
print(obj.maxMoves(grid = [[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]))