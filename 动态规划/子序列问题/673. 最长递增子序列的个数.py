from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        ans = 0
        for i in range(1, len(nums)):
            j = i - 1
            while j >= 0:
                if nums[i] > nums[j]:
                    dp[i] += dp[j]
                    break
                j -= 1
            ans = max(ans, dp[i])
        return ans

obj = Solution()
print(obj.findNumberOfLIS([1,3,5,4,7]))