from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0] * n for _ in range(n)]
        i, j, count = 0, 0, 1
        while n > 1:
            for _ in range(n - 1):
                ans[i][j] = count
                j += 1
                count += 1

            for _ in range(n - 1):
                ans[i][j] = count
                i += 1
                count += 1

            for _ in range(n - 1):
                ans[i][j] = count
                j -= 1
                count += 1

            for _ in range(n - 1):
                ans[i][j] = count
                i -= 1
                count += 1

            n -= 2

        if n == 1:
            j += 1
            i += 1
            ans[i][j] = count

        return ans

Solution.generateMatrix(Solution,3)