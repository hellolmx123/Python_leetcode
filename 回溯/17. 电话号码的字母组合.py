from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        MAPPING = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        def dfs(Count, Len, New):
            if Len == len(digits):
                for x in MAPPING[Count]:
                    New.append(x)
                    ans.append("".join(New))
                    New.pop()
            else:
                for n in digits[Len]:
                    count = ord(n) - ord("0")
                    for x in MAPPING[Count]:
                        New.append(x)
                        dfs(count,Len + 1,New)
                        New.pop()
        ans = []
        digits = list(digits)
        dfs(ord(digits[0]) - ord("0"), 1, [])
        return ans

obj = Solution()
print(obj.letterCombinations(digits = "23"))