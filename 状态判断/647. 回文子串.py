class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            for j in range(i - 1, len(s)):
                if s[i:j + 1] == s[j: i - 1:-1]:
                    ans += 1
                else:
                    break
        return ans


onj = Solution()
print(onj.countSubstrings(s = "aaa"))