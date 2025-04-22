class Solution:
    def deleteAndEarn(self, nums):
        if not nums:
            return 0
        # 统计每个数字出现的次数
        max_num = max(nums)
        count = [0] * (max_num + 1)
        for num in nums:
            count[num] += 1

        # 动态规划数组
        dp = [0] * (max_num + 1)
        dp[1] = count[1]

        for i in range(2, max_num + 1):
            # 状态转移方程
            dp[i] = max(dp[i - 1], dp[i - 2] + count[i] * i)

        return dp[max_num]
Solution.deleteAndEarn(Solution,nums = [3,4,2])

