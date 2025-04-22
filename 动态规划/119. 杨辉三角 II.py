def getRow(rowIndex: int) -> list:
    if rowIndex == 0:
        return [1]
    ans = [1]
    res = []
    i = 0
    while i < rowIndex:
        for j in range(len(res) - 1):
            ans[j + 1] = res[j] + res[j + 1]
        i += 1
        res = ans
        ans.append(1)
    return ans

getRow(3)