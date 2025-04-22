class Solution:
    def minimumSum(self, nums: list[int]) -> int:
        Min_count_left=[1000000001]*len(nums)
        Min_count_left[0]=nums[0]
        for i in range(1,len(nums)):
                Min_count_left[i]=min(Min_count_left[i-1],nums[i])
        Min_count_right=[1000000001]*len(nums)
        Min_count_right[-1]=nums[-1]
        for i in range(-2,-len(nums)-1,-1):
                Min_count_right[i]=min(Min_count_right[i+1],nums[i])
        ans=300000001
        for i in range(1,len(nums)):
            if Min_count_left[i]<nums[i] and nums[i]>Min_count_right[i] and nums[i]+Min_count_left[i]+Min_count_right[i]<ans:
                ans=nums[i]+Min_count_left[i]+Min_count_right[i]
        if ans==300000001:
            return -1
        else:
            return ans
Solution.minimumSum(Solution, [8,6,1,5,3])
Solution.minimumSum(Solution, [6,5,4,3,4,5])
