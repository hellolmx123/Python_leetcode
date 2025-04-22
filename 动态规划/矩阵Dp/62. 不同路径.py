class Solution:
    value = [1] * 101
    for i in range(2, 100):
        value[i] = value[i-1] * i
    def uniquePaths(self, m: int, n: int) -> int:
        return self.value[max(m, n)] // self.value[min(m, n)]

obj = Solution()
obj.uniquePaths(2,3)