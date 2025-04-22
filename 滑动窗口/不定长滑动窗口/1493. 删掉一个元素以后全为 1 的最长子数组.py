from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        zeroCount = 0
        maxLen = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeroCount += 1

            while zeroCount > 1:
                if nums[left] == 0:
                    zeroCount -= 1
                left += 1

            maxLen = max(maxLen, right - left)

        return maxLen
Solution.longestSubarray(Solution,[1,0,1,1,1,1,1,1,0,1,1,1,1,1])
Solution.longestSubarray(Solution,[0,1,1,1,0,1,1,0,1])