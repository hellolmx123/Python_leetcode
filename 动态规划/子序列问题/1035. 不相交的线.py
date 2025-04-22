from typing import List


class Solution:
    def maxUncrossedLines(self, num1: List[int], num2: List[int]) -> int:
        dp = [[0] * (len(num1) + 1) for _ in range((len(num2) + 1))]

        for i in range(1, len(num2) + 1):
            for j in range(1, len(num1) + 1):
                if num1[j - 1] == num2[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1]