from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        Stack = []
        ans = [0] * len(temperatures)
        n = len(temperatures) - 1
        while n > 0:
            if temperatures[n] <= temperatures[n - 1]:
                n -= 1
            else:
                break
        Stack.append(temperatures[n])
        for i in range(n - 1, -1, -1):
            if temperatures[i] < Stack[-1]:
                ans[i] = 1
                Stack.append(temperatures[i])
            else:
                m = 0
                while Stack:
                    if temperatures[i] >= Stack[-1]:
                        m += 1
                        Stack.pop()
                    else:
                        break
                ans[i] = ans[i + 1] + m
                Stack.append(temperatures[i])

        return ans

obj = Solution()
print(obj.dailyTemperatures(temperatures = [73,74,75,71,69,72,76,73]))