from typing import List


class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        maximumHeight.sort(reverse = True)
        ans, l = maximumHeight[0], len(maximumHeight)
        for i in range(1,len(maximumHeight)):
            maximumHeight[i] = min(maximumHeight[i-1] - 1,maximumHeight[i])
            ans += maximumHeight[i]
            if l - i > maximumHeight[i]:
                return -1
        return ans
Solution.maximumTotalSum(Solution,maximumHeight = [2,3,4,3])