from typing import List


# class Solution:
#   def partition(self, s: str) -> List[List[str]]:
#       self.ans = []
#       s = list(s)
#       self.BackCut(0,1,[],s)
#       return self.ans
#
#   def BackCut(self,l,Begin_num, New, s):
#       def IsPalindrome(nums):
#           return nums == nums[::-1]
#
#       if Begin_num == len(s) + 1 and IsPalindrome(s[l:Begin_num]):
#           self.ans.append(New[:])
#       else:
#           for i in range(Begin_num, len(s) + 1):
#               if IsPalindrome(s[l:i]):
#                   New.append("".join(s[l:i]))
#                   self.BackCut(i,i + 1, New, s) # l 要跟随r去变化
#                   New.pop()


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        self.BackTracking(0, 1, s, [], ans)
        return ans

    def BackTracking(self, left, right, s, New, ans):
        if right == len(s) and s[left:] == s[right - len(s) - 1:left - len(s) - 1:-1]:
            New.append(s[left:])
            ans.append(New[:])
            New.pop()
        elif right < len(s):
            self.BackTracking(left, right + 1, s, New, ans)
            if s[left:right] == s[right - len(s) - 1:left - len(s) - 1:-1]:
                New.append(s[left:right])
                self.BackTracking(right, right + 1, s, New, ans)
                New.pop()

obj = Solution()
print(obj.partition(s = "aab"))