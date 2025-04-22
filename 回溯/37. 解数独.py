from typing import List


class Solution:
    tag = True
    num_count = ['1','2','3','4','5','6','7','8','9']
    def solveSudoku(self, board: List[List[str]]):
        row_tag = [[True] * 9 for _ in range(9)]
        cor_tag = [[True] * 9 for _ in range(9)]
        board_tag = [[True] * 9 for _ in range(9)]
        num_tag = [[True] * 9 for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] in self.num_count:
                    num_tag[i][j] = False
                    num = ord(board[i][j]) - ord('1')
                    row_tag[i][num] = False
                    cor_tag[j][num] = False
                    board_tag[(i // 3) * 3 + j // 3][num] = False
        self.BackStack(board, row_tag, cor_tag, board_tag, num_tag, 0,0)
        return board

    def BackStack(self,board, row_tag, cor_tag, board_tag, num_tag, i, j):
        if j == 9 and i == 8:
            self.tag = False
            return
        elif j == 9:
            self.BackStack(board, row_tag, cor_tag, board_tag, num_tag, i + 1, 0)
            return

        if num_tag[i][j]:
            for n in range(9):
                if row_tag[i][n] and cor_tag[j][n] and board_tag[(i//3) * 3 + j // 3][n] and self.tag:
                    board[i][j] = self.num_count[n]
                    num_tag[i][j] = False
                    row_tag[i][n] = False
                    cor_tag[j][n] = False
                    board_tag[(i // 3) * 3 + j // 3][n] = False
                    self.BackStack(board, row_tag, cor_tag, board_tag, num_tag, i, j + 1)
                    num_tag[i][j] = True
                    row_tag[i][n] = True
                    cor_tag[j][n] = True
                    board_tag[(i // 3) * 3 + j // 3][n] = True
        else:
            self.BackStack(board, row_tag, cor_tag, board_tag, num_tag, i, j + 1)

obj = Solution()
print(obj.solveSudoku(board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))