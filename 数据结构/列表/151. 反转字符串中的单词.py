from typing import List


class Solution:
    def reverseWords(self, s: str) -> str:
        def reverseString(s: List[str]):
            left, right = 0,len(s) - 1
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            return s

        s_list = s.split(" ")
        s_list = reverseString(s_list)
        while "" in s_list:
            s_list.remove(" ")
        s_list = " ".join(s_list)
        return s_list.strip(" ")

obj = Solution()
print(obj.reverseWords("a good   example"))