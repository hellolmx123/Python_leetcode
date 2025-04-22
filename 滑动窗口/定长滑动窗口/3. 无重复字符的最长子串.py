class Solution:
    def lengthOfLongestSubstring(self,s: str) -> int:
        ans,left,right=0,0,0
        while right < len(s):
            if s[right] in s[left:right]:
                ans=max(right-left,ans)
                left+=s[left:right].index(s[right])+1
            right+=1
        ans=max(right-left,ans)
        return ans

Solution.lengthOfLongestSubstring(Solution,s ="aab")