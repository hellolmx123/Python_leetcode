from typing import List


class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        dp_positive = [[0] * len(grid[0]) for _ in range(len(grid))]
        dp_negative = [[0] * len(grid[0]) for _ in range(len(grid))]
        tag_zero = [[False] * len(grid[0]) for _ in range(len(grid))]
        if grid[0][0] > 0:
            dp_positive[0][0] = grid[0][0]
        elif grid[0][0] < 0:
            dp_negative[0][0] = grid[0][0]
        else:
            return 0

        for i in range(1, len(grid[0])):
            if grid[0][i] > 0:
                dp_positive[0][i] = dp_positive[0][i - 1] * grid[0][i]
                dp_negative[0][i] = dp_negative[0][i - 1] * grid[0][i]
            elif grid[0][i] < 0:
                dp_positive[0][i] = dp_negative[0][i - 1] * grid[0][i]
                dp_negative[0][i] = dp_positive[0][i - 1] * grid[0][i]
            else:
                tag_zero[0][i] = True

        for i in range(1, len(grid)):
            if grid[i][0] > 0:
                dp_positive[i][0] = dp_positive[i - 1][0] * grid[i][0]
                dp_negative[i][0] = dp_negative[i - 1][0] * grid[i][0]
            elif grid[i][0] < 0:
                dp_positive[i][0] = dp_negative[i - 1][0] * grid[i][0]
                dp_negative[i][0] = dp_positive[i - 1][0] * grid[i][0]

        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                if grid[i][j] > 0:
                    dp_positive[i][j] = max(dp_positive[i - 1][j], dp_positive[i][j - 1]) * grid[i][j]
                    dp_negative[i][j] = min(dp_negative[i - 1][j], dp_negative[i][j - 1]) * grid[i][j]
                elif grid[i][j] < 0:
                    dp_positive[i][j] = min(dp_negative[i - 1][j], dp_negative[i][j - 1]) * grid[i][j]
                    dp_negative[i][j] = max(dp_positive[i - 1][j], dp_positive[i][j - 1]) * grid[i][j]

        if dp_positive[-1][-2] > 0 and dp_positive[-2][-1] > 0:
            return -1
        return dp_positive[-1][-1]

obj = Solution()
print(obj.maxProductPath(grid = [[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]]))
