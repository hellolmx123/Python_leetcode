#class Solution:
#   def minDistance(self, word1: str, word2: str) -> int:
#        dp = [[0] * len(word1) for _ in range(len(word2))]
#        if word1[0] == word2[0]:
#            dp[0][0] = 1
#
#        for i in range(1, len(word2)):
#            if word2[i] == word1[0]:
#                dp[i][0] = 1
#            else:
#                dp[i][0] = dp[i - 1][0]
#
#        for i in range(1, len(word1)):
#            if word1[i] == word2[0]:
#                dp[0][i] = 1
#            else:
#                dp[0][i] = dp[0][i - 1]
#
#        for i in range(1, len(word2)):
#            for j in range(1, len(word1)):
#                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
#                if word2[i] == word1[j]:
#                    dp[i][j] += 1
#
#        return len(word1) - dp[-1][-1]


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[1] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        dp[0][0] = 0
        for i in range(1, len(word1) + 1):
            dp[i][0] += dp[i - 1][0]

        for i in range(1, len(word2) + 1):
            dp[0][i] += dp[0][i - 1]

        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                tag = 0
                if word1[i - 1] != word2[j - 1]:
                    tag = 1
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + tag

        return dp[-1][-1]


obj = Solution()
print(obj.minDistance("zoologicoarchaeologist", "zoogeologist"))