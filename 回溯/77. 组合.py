from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def combineListAppend(Begin_num,m, New):
            if m == 0:
                ans.append(New[:])
            else:
                for i in range(Begin_num, n + 1):
                    New.append(i)
                    combineListAppend(i + 1,m - 1, New)
                    New.pop()
        ans = []
        combineListAppend(1, k, [])
        return ans

obj = Solution()
print(obj.combine(n = 4, k = 2))