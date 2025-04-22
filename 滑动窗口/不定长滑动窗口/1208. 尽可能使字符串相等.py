class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        count = [0] * len(s)

        for i in range(len(s)):
            count[i] = abs(ord(s[i]) - ord(t[i]))

        left, right = 0, 1
        ans, Sum = 0, count[0]

        while right < len(s):
            Sum += count[right]
            if Sum > maxCost:
                while left < right and Sum > maxCost:
                    Sum -= count[left]
                    left += 1
            right += 1
            ans = max(ans, right - left)

        return ans

Solution.equalSubstring(Solution, s = "abcd", t = "bcdf", maxCost = 3)