from typing import List


class Solution:
    # 回溯版本
    ans = 0
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        self.ans, l = 0, len(nums)
        nums.sort()
        self.dfs(0,[],0,nums,k)
        return self.ans
    def dfs(self,Begin_count, New, L,num,k):
        if L <= len(num):
            for i in range(Begin_count, len(num)):
                if num[i] - k not in New:
                    New.append(num[i])
                    self.ans += 1
                    self.dfs(i + 1, New, L + 1,num,k)
                    New.pop()
obj = Solution()
a = obj.beautifulSubsets(nums = [2,4,6], k = 2)
print(a)
b = obj.beautifulSubsets(nums = [1], k = 1)
print(b)