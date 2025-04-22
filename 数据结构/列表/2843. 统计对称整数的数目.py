class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0
        while low <= high:
            if low < 10:
                low = 10
            elif 99 < low < 1000:
                low = 1000
            num = str(low)
            Len = len(num)
            left_sum, right_sum = 0, 0
            for i in range(Len // 2):
                left_sum += int(num[i])
                right_sum += int(num[- i - 1])
            if left_sum == right_sum:
                ans += 1
            low += 1
        return ans

