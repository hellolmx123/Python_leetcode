from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        l = len(height)
        left,mid, right = 1,1,1
        count, ans = 0, 0
        while right < l or left < l:
            count = 0
            while left < l:
                if height[left] >= height[left - 1]:
                    left += 1
                else:
                    break
            mid=left
            while mid < l:
                if height[mid] <= height[mid - 1]:
                    count += height[mid]
                    mid += 1
                else:
                    break
            right = mid
            while right < l:
                if height[right] >= height[right - 1]:
                    count += height[right]
                    right += 1
                else:
                    break
            ans += min(height[left-1], height[right-1]) * (right - left-1) - count+height[right-1]
            left=right
        return ans

Solution.trap(Solution,[4,2,0,3,2,5])