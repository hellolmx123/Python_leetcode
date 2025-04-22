from typing import List


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        Hash_Bool = [True] * len(nums)
        ans, New = [], []
        count = 0
        while count != len(nums):
            for i in range(len(nums)):
                if nums[i] != 0 and Hash_Bool[nums[i]]:
                    count += 1
                    New.append(nums[i])
                    Hash_Bool[nums[i]] = False
                    nums[i] = 0
            ans.append(New[:])
            New = []
            Hash_Bool = [True] * len(nums)
        return ans
obj = Solution()
print(obj.findMatrix(nums = [1,3,4,1,2,3,1]))