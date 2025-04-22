from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [1] + [0] * amount
        for x in coins:
            for i in range(amount + 1 - x):
                if dp[i] != 0:
                    dp[i + x] += dp[i]
        return dp[-1]

obj = Solution()
a = obj.change(4,[1, 2, 3])
print(a)