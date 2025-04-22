from typing import List


class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        dp = [[0] * len(grid[0]) for _ in range(2)]
        for i in range(1, len(grid)): # 当前处于第几层
            for j in range(len(grid[0])): # 当前是算第i层的哪个元素
                data = moveCost[grid[i - 1][0]][j] + grid[i - 1][0] + dp[(i - 1) % 2][0]
                for m in range(1, len(grid[0])): # 计算上层第m个元素到第i个元素的代价
                    data = min(data, moveCost[grid[i - 1][m]][j] + grid[i - 1][m] + dp[(i - 1) % 2][m])
                dp[i % 2][j] = data

        for i in range(len(grid[0])):
            dp[(len(grid) - 1) % 2][i] += grid[-1][i]

        return min(dp[(len(grid) - 1) % 2])

obj = Solution()
print(obj.minPathCost(grid = [[5,1,2],[4,0,3]], moveCost = [[12,10,15],[20,23,8],[21,7,1],[8,1,13],[9,10,25],[5,3,2]]))