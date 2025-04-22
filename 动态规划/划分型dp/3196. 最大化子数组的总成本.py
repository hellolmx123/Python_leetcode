from typing import List


class Solution:
    def maximumTotalCost(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [[nums[0]] * 2 for _ in range(len(nums))]
        dp[1][0] = nums[0] + nums[1]
        dp[1][1] = nums[0] - nums[1]
        for i in range(2, len(nums)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1]) + nums[i]
            dp[i][1] = max(dp[i - 2][0], dp[i - 2][1]) + nums[i - 1] - nums[i]
        return max(dp[-1])
obj = Solution()
print(obj.maximumTotalCost(nums = [1,-2,3,4]))