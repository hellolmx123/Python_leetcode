from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        row_count, cur_count = [0] * n, [0] * n
        row_cur_count = [0] * (2 * n - 1)
        cur_row_count = [0] * (2 * n - 1)
        New = [['.'] * n for _ in range(n)]
        ans = []
        self.StackBacking(n, row_count, cur_count, row_cur_count, cur_row_count, New, ans, 0)
        return ans

    def StackBacking(self, n, row_count, cur_count, row_cur_count, cur_row_count, New, ans, count):
        """
        :param n: 棋盘的大小
        :param row_count: 每列是不是有皇后，第 i 列有皇后则row_count[i] = 1
        :param cur_count: 每行是不是有皇后，第 i 行有皇后则row_count[i] = 1
        :param row_cur_count: 每个斜线是不是有皇后， row_cur_count[k] = 1 代表第 i - j = k这根斜线上有皇后
        :param cur_row_count: 每个斜线是不是有皇后， cur_row_count[k] = 1 代表第 j + i = k这根斜线上有皇后
        :param New: 每次输入的棋盘
        :param ans: 输出答案
        :param count: 记录当前皇后数量,同时也表示第几列皇后
        :return: 无
        """
        if count == n:
            new = [""] * n
            for i in range(n):
                new[i] = ''.join(New[i])
            ans.append(new[:])
            return
        for i in range(n):
            if row_count[count] == 0 and cur_count[i] == 0 and row_cur_count[i - count] == 0 and cur_row_count[count + i] == 0:
                row_count[count] = 1
                cur_count[i] = 1
                row_cur_count[i - count] = 1
                cur_row_count[count + i] = 1
                New[count][i] = 'Q'
                self.StackBacking(n, row_count, cur_count, row_cur_count, cur_row_count, New, ans, count + 1)
                row_count[count] = 0
                cur_count[i] = 0
                row_cur_count[i - count] = 0
                cur_row_count[count + i] = 0
                New[count][i] = '.'

obj = Solution()
print(obj.solveNQueens(20))