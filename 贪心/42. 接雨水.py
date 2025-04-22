from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        left_count, right_count = [0] * len(height), [0] * len(height)
        left_count[0], right_count[-1] = height[0], height[-1]
        for i in range(1, len(height)):
            left_count[i] = max(left_count[i - 1], height[i])
            right_count[len(height) - 1 - i] = max(right_count[len(height) - i], height[len(height) - 1 - i])

        for i in range(len(height)):
            ans += max(min(left_count[i], right_count[i]) - height[i], 0)
        left_count[0], right_count[-1] = 0, 0
        return ans

obj = Solution()
print(obj.trap([4,2,0,3,2,5]))