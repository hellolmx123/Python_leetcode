from cmath import inf
from typing import List


class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = 10 ** 9 + 7
        n, m = len(board), len(board[0])
        dp = [[[-inf] * 2 for _ in range(m + 1)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if board[i - 1][j - 1] == 'X':
                    dp[i][j] = [-inf, -inf]
                    continue
                elif board[i - 1][j - 1] == 'E':
                    dp[i][j] = [0, 1]
                    continue
                elif board[i - 1][j - 1] == 'S':
                    dp[i][j][0] = max(dp[i - 1][j][0], dp[i][j - 1][0])
                    dp[i][j][0] = dp[i][j][0] % MOD
                    if dp[i - 1][j][0] == dp[i][j - 1][0]:
                        dp[i][j][1] = (dp[i - 1][j][1] + dp[i][j - 1][1]) % MOD
                    else:
                        dp[i][j][1] = 1
                    break

                dp[i][j][0] = max(dp[i - 1][j][0], dp[i][j - 1][0]) + ord(board[i - 1][j - 1]) - ord('0')
                dp[i][j][0] = dp[i][j][0] % MOD
                if dp[i - 1][j][0] == dp[i][j - 1][0]:
                    dp[i][j][1] = (dp[i - 1][j][1] + dp[i][j - 1][1]) % MOD
                else:
                    dp[i][j][1] = 1

        return dp[-1][-1] if dp[-1][-1][0] >= 0 else [0, 0]

obj = Solution()
print(obj.pathsWithMaxScore(board = ["EX","XS"]))