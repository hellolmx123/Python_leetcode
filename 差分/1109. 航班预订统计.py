from typing import List

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans=[0]*n
        for First_Last_Seats in bookings:
            ans[First_Last_Seats[0]-1]+=First_Last_Seats[2]
            if First_Last_Seats[1]<n-1:
                ans[First_Last_Seats[1]]-=First_Last_Seats[2]
        for i in range(n-1):
            ans[i+1]+=ans[i]
        return ans

Solution.corpFlightBookings(Solution,[[1,2,10],[2,3,20],[2,5,25]],5)