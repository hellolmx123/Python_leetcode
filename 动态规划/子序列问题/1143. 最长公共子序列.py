class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text1) + 1) for _ in range((len(text2) + 1))]

        for i in range(1, len(text2) + 1):
            for j in range(1, len(text1) + 1):
                if text1[j - 1] == text2[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1]

obj = Solution()
print(obj.longestCommonSubsequence(text1 = "bsbininm", text2 = "jmjkbkjkv"))