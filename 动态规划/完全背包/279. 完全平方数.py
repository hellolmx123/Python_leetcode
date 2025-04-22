from cmath import inf


class Solution:
    dp = [inf] * 10001
    for i in range(101):
        dp[i ** 2] = 1
    for i in range(10001):
        for j in range(i // 2, i):
            dp[i] = min(dp[i],dp[j] + dp[i - j])
    def numSquares(self, n: int) -> int:
        return int(self.dp[n])
obj = Solution()
print(obj.numSquares(12))
