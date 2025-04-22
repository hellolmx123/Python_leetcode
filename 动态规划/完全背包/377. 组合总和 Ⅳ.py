from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [1] + [0] * target
        for i in range(target + 1):
            for x in nums:
                if 0 <= i - x < target + 1:
                    dp[i] += dp[i - x]
        return dp[-1]
obj = Solution()
print(obj.combinationSum4([1,2,3], 4))