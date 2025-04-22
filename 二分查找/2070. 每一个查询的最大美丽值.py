from bisect import bisect_right, bisect_left
from typing import List


class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        def Quick(nums: list[list[int]], left: int, right: int):
            tag = nums[left]
            while left < right:
                while (nums[right][0] > tag[0] or (
                        nums[right][0] == tag[0] and nums[right][1] <= tag[1])) and left < right:
                    right -= 1
                nums[left] = nums[right]
                while (nums[left][0] < tag[0] or (nums[left][0] == tag[0] and nums[left][1] > tag[1])) and left < right:
                    left += 1
                nums[right] = nums[left]
            nums[left] = tag
            return left

        def QuickSort(nums: list[list[int]], left: int, right: int):
            if left < right:
                mid = Quick(nums, left, right)
                QuickSort(nums, left, mid - 1)
                QuickSort(nums, mid + 1, right)


        QuickSort(items, 0, len(items) - 1)
        max_count = items[0][1]
        for i in range(len(items)):
            max_count = max(max_count, items[i][1])
            items[i][1] = max_count

        ans = [0] * len(queries)
        for i in range(len(queries)):
            num = bisect_left(items, [queries[i], 0])
            if queries[i] >= items[min(num,len(items) - 1)][0]:
                ans[i] = items[min(num,len(items) - 1)][1]
            elif i > 0:
                ans[i] = ans[i - 1]
        return ans

obj = Solution()
print(obj.maximumBeauty(items = [[1,2],[3,2],[2,4],[5,6],[3,5]], queries = [1,2,3,4,5,6]))