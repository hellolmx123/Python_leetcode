class Solution:
    def MinDelete(self,Str:str) -> int:
        dp = [[0] * len(Str) for _ in range(len(Str) + 1)]
        # dp[i][j] 的含义是指 以 i 开头 j 结尾的数组里面括号匹配的最大长度
        for i in range(len(Str) - 1, -1, -1):
            for j in range(i, len(Str)):
                if [Str[i], Str[j]] in [['(', ')'], ['{', '}'], ['[', ']']]: # 如果 Str[i] 与 Str[j] 匹配
                    dp[i][j] = dp[i + 1][j - 1] + 2
                    # 因为 i 与 j 已经匹配
                    # 那么数组Str[i:j + 1]中最大匹配数量就是 2 加上Str[i + 1:j]中最大匹配数量
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
                    # 因为 i 与 j 没有匹配
                    # 那么数组Str[i:j + 1]中最大匹配数量就是
                    # Str[i + 1:j]中最大匹配数量和Str[i:j + 1]中最大匹配数量的最大值

        return len(Str) - dp[0][-1]

obj = Solution()
print(obj.MinDelete('{[()]}')) # 不需要删除操作，已经满足 最后输出 0

print(obj.MinDelete('{(})')) # 删除位置为 1,3 的括号满足 最后输出 2

print(obj.MinDelete('{[((])]}'))# 删除位置为 3,4 的括号满足 最后输出 2