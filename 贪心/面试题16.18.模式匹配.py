from typing import List


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        # 判断每个小孩分到 i 个糖果时是否可以满足要求
        def check(i: int) -> bool:
            res = 0
            for c in candies:
                res += c // i
            return res >= k

        # 二分查找
        l = 1
        r = max(candies) + 1
        while l < r:
            mid = l + (r - l) // 2
            if check(mid):
                l = mid + 1
            else:
                r = mid
        return l - 1

