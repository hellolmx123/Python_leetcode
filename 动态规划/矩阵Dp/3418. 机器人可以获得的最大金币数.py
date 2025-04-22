from typing import List


class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m = len(coins)
        n = len(coins[0])
        dp = [[[-1001] * 3 for _ in range(n + 1)] for _ in range(m + 1)]
        dp[0][1] = [0,0,0]
        dp[1][0] = [0,0,0]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j][0] = max(dp[i - 1][j][0] , dp[i][j - 1][0]) + coins[i - 1][j - 1]
                if coins[i - 1][j - 1] < 0:
                    dp[i][j][1] = max(dp[i - 1][j][0] , dp[i][j - 1][0], dp[i - 1][j][1] + coins[i - 1][j - 1], dp[i][j - 1][1] + coins[i - 1][j - 1])
                    dp[i][j][2] = max(dp[i - 1][j][1] , dp[i][j - 1][1], dp[i - 1][j][2] + coins[i - 1][j - 1], dp[i][j - 1][2] + coins[i - 1][j - 1])
                else:
                    dp[i][j][1] = max(dp[i - 1][j][1] , dp[i][j - 1][1]) + coins[i - 1][j - 1]
                    dp[i][j][2] = max(dp[i - 1][j][2] , dp[i][j - 1][2]) + coins[i - 1][j - 1]

        return max(dp[-1][-1])

obj = Solution()
print(obj.maximumAmount(coins = [[-7,12,12,13],[-6,19,19,-6],[9,-2,-10,16],[-4,14,-10,-9]]))