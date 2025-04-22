from astroid import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def merge(interval: List[List[int]]) -> List[List[int]]:
            interval.sort()
            ans=[]
            for num in interval:
                if ans and num[0]<=ans[-1][1]:
                    ans[-1][1]=max(num[1],ans[-1][1])
                else:
                    ans.append(num)
            return ans

        intervals.append(newInterval)
        return merge(intervals)