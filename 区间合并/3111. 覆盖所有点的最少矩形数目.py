class Solution:
    def minRectanglesToCoverPoints(self, points: list[list[int]], w: int) -> int:
        points.sort(key=lambda p: p[0])
        ans = 0
        x2 = -1
        for x, _ in points:
            if x > x2:
                ans += 1
                x2 = x + w
        return ans

Solution.minRectanglesToCoverPoints(Solution,[[7,4],[8,1]],2)