class Solution:
    def countCollisions(self, d: str) -> int:
        Stack=["A"]
        ans=0
        for i in range(len(d)):
            Stack.append(d[i])
            if d[i]=="L"and Stack[-2]=="S":
                ans+=1
                Stack[-1]="S"
            elif d[i]=="L" and Stack[-2]=="R":
                ans+=1
                while len(Stack)>2:
                    if Stack[-2]=="R":
                        ans+=1
                        Stack=Stack[:-1]
                        Stack[-1]="S"
                    else:
                        break
            elif d[i]=="S" and Stack[-2]=="R":
                while len(Stack)>2:
                    if Stack[-2]=="R":
                        ans+=1
                        Stack=Stack[:-1]
                        Stack[-1]="S"
                    else:
                        break
        print(ans)
        return ans

Solution.countCollisions(Solution,d = "RLRSLL")