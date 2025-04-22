from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        s = 0
        ans = 0
        count_list = defaultdict(int)
        for x in nums:
            s += x
            ans += count_list[s - k]
            count_list[s] += 1
        return ans

obj = Solution()
print(obj.subarraySum(nums = [1,1,1], k = 2))