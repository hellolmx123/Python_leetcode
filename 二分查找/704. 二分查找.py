from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = -1, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
            else:
                return mid
        return -1