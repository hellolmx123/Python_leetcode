from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        tag = [-1] * (max(nums2) + 1)
        Stack = []
        for i in range(len(nums2)):
            if not Stack:
                Stack.append(i)
                continue
            while Stack and nums2[i] > nums2[Stack[-1]]:
                tag[nums2[Stack[-1]]] = nums2[i]
                Stack.pop()
            Stack.append(i)
        ans = [0] * len(nums1)
        for i in range(len(nums1)):
            ans[i] = tag[nums1[i]]

        return ans
obj = Solution()
print(obj.nextGreaterElement(nums1 = [4,1,2], nums2 = [1,3,4,2]))