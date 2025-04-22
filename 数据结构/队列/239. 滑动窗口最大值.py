from bisect import bisect_left
from typing import List


class Solution:
    def MaxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        Queue = nums[:k]
        Queue.sort()
        ans = []
        for i in range(len(nums) - k):
            Queue.insert(bisect_left(Queue,nums[i + k]), nums[i + k])
            Queue.remove(nums[i])
            ans.append(Queue[-1])
        return ans

obj = Solution()
print(obj.MaxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3))