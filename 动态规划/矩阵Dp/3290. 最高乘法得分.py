from typing import List


class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        dp = [[0] * len(b) for _ in range(4)]
        dp[0][0] = a[0] * b[0]
        for i in range(1, len(b)):
            dp[0][i] = max(a[0] * b[i], dp[0][i - 1])

        for i in range(1, 4):
            for j in range(i, len(b)):
                if i == j:
                    dp[i][j] = dp[i - 1][j - 1] + a[i] * b[j]
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - 1] + a[i] * b[j])

        return dp[-1][-1]

obj = Solution()
print(obj.maxScore(a = [3,2,5,6], b = [2,-6,4,-5,-3,2,-7]))