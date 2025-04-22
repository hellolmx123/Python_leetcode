class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        def f(s:list):
            if not s:
                return "",-1
            Tag=s[-1]
            L=1
            for I in range(-2,-len(s)-1,-1):
                if s[I]!=Tag:
                    break
                L+=1
            return Tag,L

        Stack=[]
        tag=""
        l=1
        for i in s:
            Stack.append(i)
            if i == tag and l==k-1:
                Stack=Stack[:-k]
                tag,l=f(Stack)
            elif i==tag and l<k-1:
                l+=1
            else:
                tag=i
                l=1
        print("".join(Stack))
        return "".join(Stack)

Solution.removeDuplicates(Solution,"deeedbbcccbdaa",3)

