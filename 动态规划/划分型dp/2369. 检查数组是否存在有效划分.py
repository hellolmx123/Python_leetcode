from typing import List


class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        dp = [True] + [False] * len(nums)

        if nums[0] == nums[1]:
            dp[2] = True
        for i in range(2, len(nums)):
            if dp[i - 1] and nums[i] == nums[i - 1]:
                dp[i + 1] = True
            if dp[i - 2] and (nums[i] == nums[i - 1] == nums[i - 2] or nums[i] - 1 == nums[i - 1] == nums[i - 2] + 1):
                dp[i + 1] = True

        return dp[-1]
obj = Solution()
print(obj.validPartition([1,1,1,1,2,3]))