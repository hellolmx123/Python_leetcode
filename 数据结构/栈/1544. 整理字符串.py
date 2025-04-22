class Solution:
    def makeGood(self, s: str) -> str:
        stack=[]
        for i in s:
            if not stack:
                stack.append(i)
            elif abs(ord(i)-ord(stack[-1]))==32:
                stack.pop()
            else:
                stack.append(i)
        return "".join(stack)

Solution.makeGood(Solution,"leEeetcode")