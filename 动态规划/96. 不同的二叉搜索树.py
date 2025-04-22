# class Solution:
#     dp = [0] * 20
#     dp[0] = 1
#     dp[1] = 1
#     for i in range(2, 20):
#         for left in range(i):
#             dp[i] += dp[left] * dp[i - left - 1]
#
#     def numTrees(self, n: int) -> int:
#         return self.dp[n]
#

class Solution:
    dp = [1] * 20
    for i in range(2, 20):
        dp[i] = 0
        for j in range(i):
            dp[i] += dp[j] * dp[i - j - 1]
    def numTrees(self, n: int) -> int:
        return self.dp[n]

obj = Solution()
print(obj.numTrees(4))