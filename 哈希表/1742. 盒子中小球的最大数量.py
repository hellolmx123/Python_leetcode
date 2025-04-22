class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        count=[0]*36
        Sum=0
        for i in range(lowLimit,highLimit+1):
            Sum=0
            while i>=10:
                x=i%10
                i=(i-x)//10
                Sum+=x
            Sum+=i
            count[Sum]+=1
        return max(count)

Solution.countBalls(Solution,1,10)