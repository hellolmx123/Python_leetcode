from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        left, right = 2, len(nums) - 1
        ans = []
        self.BackTracking(left, right, nums, ans)
        return ans

    def BackTracking(self, left, right, nums, ans):
        if left >= right - 1:
            return
        m = self.bisect_search(nums, left + 1, right - 1, -(nums[left] + nums[right]))
        if nums[m] + nums[left] + nums[right] == 0:
            ans.append([nums[left], nums[m], nums[right]])
            while 0 < left < right - 1 and nums[left - 1] == nums[left]:
                left += 1
            while nums[right + 1] == nums[right] and left < right - 1 < len(nums) - 1:
                right -= 1
            self.BackTracking(left, right - 1, nums, ans)
        elif nums[m] + nums[left] + nums[right] < 0:
            while 0 < left < right - 1 and nums[left - 1] == nums[left]:
                left += 1
            self.BackTracking(left + 1, right, nums, ans)
        else:
            while nums[right + 1] == nums[right] and left < right - 1 < len(nums) - 1:
                right -= 1
            self.BackTracking(left, right - 1, nums, ans)
    def bisect_search(self, nums, left, right, target):
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
            else:
                return mid
        return left

obj = Solution()
print(obj.threeSum(nums = [2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10]))