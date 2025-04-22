from bisect import bisect_right
class Solution:
    def answerQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        nums.sort()
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
        for i,val in enumerate(queries):
            queries[i]=bisect_right(nums,val)
        return queries
Solution.answerQueries(Solution,[4,5,2,1],[3,10,21])

