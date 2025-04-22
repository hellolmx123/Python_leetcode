class Solution:
    def validNumber(self, s: str) -> bool:
        number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        count = ['+', '-']

        def IsWholeNumber(nums):
            if not nums:
                return False
            tag = False
            n = 0
            if nums[0] not in number and nums[0] not in count and nums[0] != ' ':
                return False
            elif nums[0] in count:
                n = 1
            for i in range(n, len(nums)):
                if nums[i] not in number :
                    return False
                elif nums[i] in number:
                    tag = True
            return tag

        def IsFloat(nums):
            if IsWholeNumber(nums):
                return True
            elif len(nums) == 1:
                return False
            for i in range(len(nums)):
                if nums[i] not in number and nums[i] not in count and nums[i] not in ['.', ' ']:
                    return False
                elif nums[i] == '.':
                    if i == 0:
                        if nums[i + 1] not in number:
                            return False
                        elif IsWholeNumber(nums[i + 1:]):
                            return True
                    elif i == len(nums) - 1:
                        if nums[i - 1] not in number:
                            return False
                        elif IsWholeNumber(nums[:i]):
                            return True
                    elif i == 1:
                        if (nums[0] in count or nums[0] in number) and IsWholeNumber(nums[i + 1:]):
                            return True
                    else:
                        if nums[i + 1] not in number and nums[i - 1] not in number:
                            return False
                        elif IsWholeNumber(nums[:i]) and IsWholeNumber(nums[i + 1:]):
                            return True
            return False
        s = s.strip(' ')
        if IsFloat(s) or IsWholeNumber(s):
            return True

        for i in range(len(s)):
            if s[i] not in number and s[i] not in count and s[i] not in [".", 'e', 'E']:
                return False
            elif s[i] in ['e', 'E']:
                if (IsWholeNumber(s[:i]) or IsFloat(s[:i])) and IsWholeNumber(s[i + 1:]):
                    return True
        return False

obj = Solution()
print(obj.validNumber("+.8"))