class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # KMP字符串匹配
        next_count = [0] * len(needle)
        k = 0
        for i in range(1, len(needle)):
            while needle[i] != needle[k] and k > 0:
                k = next_count[k - 1]
            if needle[i] == needle[k]:
                k += 1
            next_count[i] = k
        # 建立next_count 数组

        
        # KMP字符串匹配

        return -1

obj = Solution()
print(obj.strStr(haystack = "leetcode", needle = "bbbbbbaa"))