class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        left,right=0,0
        while right<len(nums):
            if nums[right]==nums[left] and right<len(nums):
                if right-left==2 and right<len(nums):
                    nums.pop(right)
                right += 1
            else:
                left=right
                right+=1
        return len(nums)

nums=[1,1,1,2,2,3]
data=Solution.removeDuplicates(Solution,nums)
print(data)