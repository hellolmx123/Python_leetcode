class Solution:
    def minSwaps(self, s: str) -> int:
        left, right = 0, len(s) - 1
        left_count, right_count = 0, 0
        ans = 0
        s = list(s)
        while left < right:
            while not (s[left] == ']' and left_count == 0) and left < right:
                if s[left] == '[':
                    left_count += 1
                else:
                    left_count -= 1
                left += 1
            while not (s[right] == '[' and right_count == 0) and left < right:
                if s[right] == ']':
                    right_count += 1
                else:
                    right_count -= 1
                right -= 1
            s[left], s[right] = s[right], s[left]
            if right - left > 2:
                ans += 1
            right -= 1
            left += 1
        return ans

obj = Solution()
print(obj.minSwaps("][]["))
print(obj.minSwaps("]]][[["))
print(obj.minSwaps("[]"))
print(obj.minSwaps("][[][[][[][][[]]]]"))