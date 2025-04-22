from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        count = [1] * len(nums)
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                for j in range(i):
                    count[j] += 1
                    j += 1
        return max(count)

obj = Solution()
print(obj.lengthOfLIS(nums = [4,10,4,3,8,9]))