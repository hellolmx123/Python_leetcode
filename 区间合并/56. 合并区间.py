from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n=len(intervals)
        intervals.sort()
        ans=[]
        left,right=intervals[0][0],intervals[0][1]
        for num in intervals:
            l,r=num[0],num[1]
            if l<=right:
                right=max(r,right)
            else:
                ans.append([left,right])
                left=num[0]
                right=num[1]
        ans.append([left,right])
        return ans
Solution.merge(Solution,[[1,3],[2,6],[8,10],[15,18]])