class Solution:
    ans = 0
    dp = [[1] for _ in range(10001)]
    for i in range(1, 10001):
        for j in range(2, i + 1):
            if i % j == 0:
                dp[i].append(j)
    def idealArrays(self, n: int, maxValue: int) -> int:
        MOD = 10 ** 9 + 7
        self.ans = 0
        for i in range(1, maxValue + 1):
            self.BackTracking(i, n - 1, 1, MOD)
        return self.ans
    def BackTracking(self, nums, n, Len, MOD):
        if Len == n:
            self.ans += len(self.dp[nums]) % MOD
            return
        for x in self.dp[nums]:
            self.BackTracking(x, n , Len + 1, MOD)

obj = Solution()
print(obj.idealArrays(5, 3))