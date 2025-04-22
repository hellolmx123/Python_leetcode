# class Solution:
#     def numDistinct(self, t: str, s: str) -> int:
#         dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
#
#         for i in range(len(t) + 1):
#             dp[0][i] = 1
#
#         for i in range(1, len(s) + 1):
#             for j in range(i, len(t) + 1):
#                 if s[i - 1] == t[j - 1]:
#                     dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
#                 else:
#                     dp[i][j] = dp[i][j - 1]
#         return dp[-1][-1] % 1000000007
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0] * (len(s) + 1) for _ in range(len(t) + 1)]

        for i in range(len(s) + 1):
            dp[0][i] = 1

        for i in range(1, len(t) + 1):
            for j in range(i, len(s) + 1):
                if t[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]

        return dp[-1][-1] % (10 ** 9 + 7)

obj = Solution()
print(obj.numDistinct(s = "rabbbit", t = "rabbit"))