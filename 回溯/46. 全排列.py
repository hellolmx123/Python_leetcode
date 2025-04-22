from typing import List


# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         ans = []
#         self.BackTracking(nums, 0, [], ans)
#         return ans
#
#     def BackTracking(self, nums: List[int], l: int, New: List[int], ans: List[List[int]]):
#         if l == len(nums):
#             ans.append(New[:])
#             return
#         for i in nums:
#             if i not in New:
#                 New.append(i)
#                 self.BackTracking(nums, l + 1, New, ans)
#                 New.pop()

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        tag = [True] * len(nums)
        ans = []
        self.Backtracking(nums, [], tag, ans)
        return ans
    def Backtracking(self, nums, New, tag, ans):
        if len(New) == len(nums):
            ans.append(New[:])
            return
        for i in range(len(nums)):
            if tag[i]:
                New.append(nums[i])
                tag[i] = False
                self.Backtracking(nums, New, tag, ans)
                New.pop()
                tag[i] = True


obj = Solution()
print(obj.permute([1,2,3]))