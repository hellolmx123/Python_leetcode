class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 == 1:
            return False
        l, r, m = 0, 0, 0
        for i in range(len(s)):
            if locked[i] == '1':
                if s[i] == '(':
                    l += 1
                else:
                    r += 1
            else:
                m += 1
            if l < r - m:
                return False
        l1, r1, m1 = 0, 0, 0
        for i in range(len(s) - 1, -1, -1):
            if locked[i] == '1':
                if s[i] == ')':
                    r1 += 1
                else:
                    l1 += 1
            else:
                m1 += 1
            if r1 < l1 - m1:
                return False
        return True if m >= l - r and m1 >= r1 - l1 else False



obj = Solution()
print(obj.canBeValid(s = "))()))", locked = "010100"))
# (((())(((())
# 111111010111