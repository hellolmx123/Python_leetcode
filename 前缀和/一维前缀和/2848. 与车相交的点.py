class Solution:
    def numberOfPoints(self, nums: list[list[int]]) -> int:
        nums.sort()
        Max,New=nums[0][1],nums[0][0]
        ans=0
        for num in nums:
            if num[0] <= Max < num[1]:
                Max=num[1]
            elif num[0]>Max:
                ans+=Max-New+1
                Max,New=num[1],num[0]
        ans+=Max-New+1
        print(ans)
        return ans
Solution.numberOfPoints(Solution,[[9,9],[2,8],[5,8],[3,5],[2,2],[7,9],[5,10]])