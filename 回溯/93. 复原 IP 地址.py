from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # 判断输入的数字是否合法
        def IsNum(strs:str):
            if strs[0] == '0' and len(strs) == 1:
                return True
            elif strs[0] == '0':
                return False
            elif 0 <= int(strs) <= 255:
                return True
            else:
                return False

        ans = []
        for i in range(1, min(len(s), 4)):
            New = ""
            if IsNum(s[0:i]):
                New += s[0:i] + '.'
            else:
                break
            for j in range(i + 1, min(len(s), i + 4)):
                New = New[:i + 1]
                if IsNum(s[i:j]):
                    New += s[i:j] + '.'
                else:
                    break
                for m in range(j + 1, min(len(s), j + 4)):
                    New = New[:j + 2]
                    if IsNum(s[j:m]):
                        New += s[j:m] + '.'
                    else:
                        break
                    if len(s) - m <= 3 and IsNum(s[m:]):
                        New += s[m:]
                        ans.append(New)
                    else:
                        continue
        return ans

obj = Solution()
print(obj.restoreIpAddresses(s = "101023"))