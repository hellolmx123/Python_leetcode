from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def combination(begin_num,l, Sum,New):
            if l == k and Sum == n:
                ans.append(New[:])
            elif l < k:
                for i in range(begin_num, min(10, n - Sum + 1)):
                    New.append(i)
                    combination(i + 1, l + 1, Sum + i, New)
                    New.pop()
        ans = []
        combination(1, 0, 0, [])
        return ans

obj = Solution()
print(obj.combinationSum3(k = 3, n = 9))