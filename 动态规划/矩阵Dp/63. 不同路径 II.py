from typing import List


# class Solution:
#     def work(self,obstacleGrid,i:int,j:int):
#         if i+1<len(obstacleGrid) and j+1<len(obstacleGrid[0]):
#             if obstacleGrid[i+1][j]==0 and obstacleGrid[i][j+1]==0:
#                 return Solution.work(self,obstacleGrid,i+1,j)+Solution.work(self,obstacleGrid,i,j+1)
#             elif obstacleGrid[i][j+1]==0 and obstacleGrid[i+1][j]!=0:
#                 return Solution.work(self,obstacleGrid,i,j+1)
#             elif obstacleGrid[i][j+1]!=0 and obstacleGrid[i+1][j]==0:
#                 return Solution.work(self,obstacleGrid,i+1,j)
#             else:
#                 return 0
#         elif i+1<len(obstacleGrid) and j+1==len(obstacleGrid[0]):
#             if obstacleGrid[i+1][j]==0:
#                 return Solution.work(self,obstacleGrid,i+1,j)
#             else:
#                 return 0
#         elif i+1==len(obstacleGrid) and j+1<len(obstacleGrid[0]):
#             if obstacleGrid[i][j+1]==0:
#                 return Solution.work(self,obstacleGrid,i,j+1)
#             else:
#                 return 0
#         elif i+1==len(obstacleGrid) and j+1==len(obstacleGrid[0]):
#             return 1
#         else:
#             return 0
#
#     def uniquePathsWithObstacles_1(self, obstacleGrid) -> int:
#         if obstacleGrid[len(obstacleGrid)-1][len(obstacleGrid[0])-1]==1 or obstacleGrid[0][0]:
#             return 0
#         return Solution.work(self,obstacleGrid,0,0)
#
#     def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
#         m, n = len(obstacleGrid), len(obstacleGrid[0])
#         dp = [[0] * (n + 1) for _ in range(m + 1)]
#         dp[1][0] = 1
#         for i in range(m):
#             for j in range(n):
#                 if not obstacleGrid[i][j]:
#                     dp[i + 1][j + 1] = dp[i][j + 1] + dp[i + 1][j]
#         return dp[-1][-1]

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = [[0] * len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
        dp[0][0] = 1
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue
                if i != 0:
                    dp[i][j] += dp[i - 1][j]
                if j != 0:
                    dp[i][j] += dp[i][j - 1]
        return dp[-1][-1]
obstacleGrid=[[0,0]]
obj = Solution()
data=obj.uniquePathsWithObstacles(obstacleGrid)
print(data)