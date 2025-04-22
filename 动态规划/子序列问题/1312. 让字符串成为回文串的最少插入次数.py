class Solution:
    def minInsertions(self, s: str) -> int:
        s_reverse = s[::-1]
        dp = [[0] * (len(s) + 1) for _ in range(len(s) + 1)]
        for i in range(1, len(s) + 1):
            for j in range(1, len(s) + 1):
                if s[i - 1] == s_reverse[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return len(s) - dp[-1][-1]

obj = Solution()
print(obj.minInsertions(s = "leetcode"))