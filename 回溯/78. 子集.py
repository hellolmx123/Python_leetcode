from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.BackTracking(nums, 0, ans, [])
        return ans


    def BackTracking(self, nums:List[int], Begin_num:int, ans:List[List[int]], New:List[int]):
        if New not in ans:
            ans.append(New[:])
        for i in range(Begin_num, len(nums)):
            New.append(nums[i])
            self.BackTracking(nums, i + 1, ans, New)
            New.pop()
            self.BackTracking(nums, i + 1, ans, New)

obj = Solution()
print(obj.subsets([0,1,2]))