from typing import List

class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        List = [0] * sum(limits) # 存贮每个List_num的中大的limits[i]个值
        n = 0 # List的指针
        for i, List_num in enumerate(grid):
            for _ in range(limits[i]):
                List[n] = max(List_num)
                n += 1
                List_num.remove(max(List_num))
        List.sort()
        return sum(List[len(List) - k: len(List)])

Solution.maxSum(Solution, grid = [[5,3,7],[8,2,6]], limits = [2,2], k = 3)