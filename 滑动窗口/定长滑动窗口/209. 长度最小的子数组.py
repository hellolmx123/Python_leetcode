from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums)<target:
            return 0
        left,right=0,1
        Sum=nums[0]
        ans=1000
        while right<len(nums) and left<len(nums):
            if Sum<target:
                Sum+=nums[right]
                right+=1
            else:
                ans=min(ans,right-left)
                Sum -= nums[left]
                left += 1
        while left<len(nums) and Sum>target:
            ans=min(ans,right-left)
            Sum -= nums[left]
            left += 1
        ans = min(ans, right - left)
        print(ans)
        return ans

Solution.minSubArrayLen(Solution,target = 7, nums = [2,3,1,2,4,3])