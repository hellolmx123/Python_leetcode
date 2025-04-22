from cmath import inf
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        ans = 0
        count = [inf,inf]
        for x in intervals:
            if x[1] > count[-1]:
                ans += 1
            else:
                count = x
        return ans

obj = Solution()
print(obj.eraseOverlapIntervals([[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]]))