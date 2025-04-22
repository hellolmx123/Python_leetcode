class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s=list(s)
        t=list(t)
        i=-1
        while i < len(s) or i <len(t):
            i+=1
            if i < len(s):
                if s[i]=="#":
                    s.pop(i-1)
                    s.pop(i)
            if i < len(t):
                if t[i]=="#":
                    t.pop(i-1)
                    t.pop(i)
        if s==t:
            return True
        else:
            return False

s,t= "cb##","d#c#"
Solution.backspaceCompare(Solution,s,t)
