class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + ord(s1[i - 1])
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        Sum1, Sum2 = 0, 0
        for x in s1:
            Sum1 += ord(x)
        for x in s2:
            Sum2 += ord(x)

        return Sum1 + Sum2 - 2 * dp[-1][-1]

obj = Solution()
print(obj.minimumDeleteSum(s1 = "sea", s2 = "eat"))