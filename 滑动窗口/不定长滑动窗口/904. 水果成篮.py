from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        tag = [fruits[0],fruits[0]]
        left,mid,right = 0,0,0
        ans = 0

        while fruits[mid] == tag[0]:
            mid += 1
            if mid == len(fruits):
                return len(fruits)
        tag[1] = fruits[mid]
        right = mid
        #初始化滑动窗口

        while right < len(fruits):
            if fruits[right] not in tag:
                ans = max(right - left, ans)

