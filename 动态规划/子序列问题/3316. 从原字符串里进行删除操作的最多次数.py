from typing import List


class Solution:
    def maxRemovals(self, source: str, pattern: str, targetIndices: List[int]) -> int:
        source = list(source)
        for i in targetIndices:
            source[i] = 'A'

        dp = [[0] * len(source) for _ in range(len(pattern))]
        if source[0] == pattern[0]:
            dp[0][0] = 1

        for i in range(len(source)):
            if source[i] == pattern[0]:
                dp[0][i] = 1
            else:
                dp[0][i] = dp[0][i - 1]

        for i in range(len(pattern)):
            if source[0] == pattern[i]:
                dp[i][0] = 1
            else:
                dp[i][0] = dp[i - 1][0]

        for i in range(1, len(pattern)):
            for j in range(1, len(source)):
                if source[j] == source[i]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return len(targetIndices) - (len(pattern) - dp[-1][-1])

obj = Solution()
print(obj.maxRemovals(source = "abbaa", pattern = "aba", targetIndices = [0,1,2]))