from typing import List


class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        ans=[[0]*(n+2) for _ in range(n+2)]
        for row1, col1, row2, col2 in queries:
            ans[row1+1][col1+1]+=1
            ans[row2+2][col2+2]+=1
            ans[row2+2][col1+1]-=1
            ans[row1+1][col2+2]-=1
        for row in range(1,n+1):
            for col in range(1,n+1):
                ans[row][col]+=ans[row-1][col]+ans[row][col-1]-ans[row-1][col-1]
        ans=ans[1:-1]
        for i,val in enumerate(ans):
            ans[i]=val[1:-1]
        return ans

Solution.rangeAddQueries(Solution,3,[[1,1,2,2],[0,0,1,1]])