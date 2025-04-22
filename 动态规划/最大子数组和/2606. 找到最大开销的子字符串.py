from typing import List


class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        count=[0]*26
        for i in range(26):
            count[i]=i+1
        for i in range(len(chars)):
            count[ord(chars[i])-ord("a")]=vals[i]
        # 创立初始字符数组

        dp=[0]*len(s)
        dp[0]=max(0,count[ord(s[0])-ord("a")])
        # 创立初始化状态方程

        for i in range(1,len(s)):
            val=count[ord(s[i])-ord("a")]
            dp[i]=max(dp[i-1]+val,val,0)
        return max(dp)

Solution.maximumCostSubstring(Solution,s = "adaa", chars = "d", vals = [-1000])