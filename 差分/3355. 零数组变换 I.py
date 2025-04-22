from typing import List


class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        l=len(nums)
        count=[0]*(l+1)
        for left,right in queries:
            count[left]-=1
            count[right+1]+=1
        for i in range(l):
            count[i+1]+=count[i]
            if count[i]+nums[i]>0:
                return False
        return True
Solution.isZeroArray(Solution,[1,0,1],[[0,2]])
