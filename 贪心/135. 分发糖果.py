from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        def candys(rating):
            candy_num = [1] * len(rating)
            for i in range(1, len(rating)):
                if rating[i] > rating[i - 1]:
                    candy_num[i] += candy_num[i - 1]
            return candy_num

        ans = 0
        left_candy_num = candys(ratings)
        right_candy_num = candys(ratings[::-1])
        for i in range(len(ratings)):
            ans += max(left_candy_num[i], right_candy_num[-i - 1])
        return ans

obj = Solution()
print(obj.candy([1,0,2,3,4,5,6,2,3,4]))