from typing import List


class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        Stack=[]
        for i in range(len(nums)):
            if not Stack:
                Stack.append(nums[i])
            elif len(Stack)%2==1 and nums[i]==Stack[-1]:
                continue
            else:
                Stack.append(nums[i])
        l=len(Stack)
        return len(nums)-l if l % 2==0 else len(nums)-l-1
Solution.minDeletion(Solution,[1,1,2,2,3,3])