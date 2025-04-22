from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def dfs(begin_num, New, l):
            if l >= 2:
                ans.append(New[:])
            for i in range(begin_num, len(nums)):
                if nums[i] >= New[-1] and nums[i] not in USet:
                    USet.add(nums[i])
                    New.append(nums[i])
                    dfs(i + 1, New, l + 1)
                    New.pop()
                    USet.remove(nums[i])
        ans = []
        USet = set()
        for i in range(len(nums)):
            dfs(i + 1,[nums[i]],1)
        return ans

obj = Solution()
print(obj.findSubsequences(nums = [4,4,3,2,1]))