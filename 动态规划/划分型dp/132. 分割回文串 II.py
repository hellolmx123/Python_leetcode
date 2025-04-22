class Solution:
    def minCut(self, s: str) -> int:
        dp = [[False] * len(s) for _ in range(len(s))]
        dp[-1][-1] = True
        for i in range(len(s) - 2, -1, -1):
            for j in range(i, len(s)):
                if i == j:
                    dp[i][j] = True
                elif s[i] == s[j]:
                    dp[i][j] = (dp[i + 1][j] and dp[i][j - 1]) or dp[i + 1][j - 1]

        dp_count = [[0] * len(s) for _ in range(len(s))]
        for i in range(len(s) - 2, -1, -1):
            for j in range(i + 1, len(s)):
                if dp[i][j]:
                    dp_count[i][j] = 0
                else:
                    dp_count[i][j] = min(dp_count[i + 1][j], dp_count[i][j - 1]) + 1
        return dp_count[0][-1]

obj = Solution()
print(obj.minCut("cabababcbc"))