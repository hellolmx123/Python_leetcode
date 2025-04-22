class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%3!=0:
            return False
        Stack=[]
        for i in range(len(s)):
            if len(Stack)>=2 and s[i]=="c":
                if Stack[-1]!='b' or Stack[-2]!='a':
                    return False
                else:
                    Stack=Stack[:-2]
            else:
                Stack.append(s[i])
        return True if len(Stack)==0 else False


Solution.isValid(Solution,"abccba")