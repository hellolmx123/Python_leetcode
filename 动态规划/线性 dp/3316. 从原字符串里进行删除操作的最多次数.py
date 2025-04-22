from cmath import inf
from functools import cache
from typing import List, Any


class Solution:
    def maxRemovals(self, source: str, pattern: str, targetIndices: List[int]) -> int:
        targetIndices = set(targetIndices)

        @cache  # 缓存装饰器，避免重复计算 dfs 的结果（记忆化）
        def dfs(i: int, j: int) -> float | int | bool | Any:
            if i < j:
                return -inf
            if i < 0:
                return 0
            res = dfs(i - 1, j) + (i in targetIndices)
            if j >= 0 and source[i] == pattern[j]:
                res = max(res, dfs(i - 1, j - 1))
            return res

        ans = dfs(len(source) - 1, len(pattern) - 1)
        dfs.cache_clear()  # 防止爆内存
        return ans

obj = Solution()
print(obj.maxRemovals(source = "bba", pattern = "bba", targetIndices = [0,1,2]))