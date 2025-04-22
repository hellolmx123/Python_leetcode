from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <=1:
            return 0
        left,right=0,0
        ans,que=0,1
        while right<len(nums):
            que *= nums[right]
            while que>=k:
                que/=nums[left]
                left+=1
            ans += right-left+1
            right+=1
        return ans

Solution.numSubarrayProductLessThanK(Solution,nums = [10,5,2,6], k = 100)