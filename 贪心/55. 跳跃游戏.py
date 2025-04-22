from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        foods = nums[0] - 1
        n = 1
        while foods > 0:
            foods = max(foods - 1, nums[n])
            if foods == 0:
                return False
            if n == len(nums) - 1:
                return True
            n += 1
        return False

obj = Solution()
print(obj.canJump([3,2,1,0,4]))