class NumMatrix:
    def __init__(self, matrix: list[list[int]]):
        m, n = len(matrix), len(matrix[0])
        s = [[0] * (n + 1) for _ in range(m + 1)]
        for i, row in enumerate(matrix):
            for j, x in enumerate(row):
                s[i + 1][j + 1] = s[i + 1][j] + s[i][j + 1] - s[i][j] + x
        self.s = s

    # 返回左上角在 (r1,c1) 右下角在 (r2,c2) 的子矩阵元素和
    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        print(self.s[r2 + 1][c2 + 1] - self.s[r2 + 1][c1] - self.s[r1][c2 + 1] + self.s[r1][c1])
        return self.s[r2 + 1][c2 + 1] - self.s[r2 + 1][c1] - self.s[r1][c2 + 1] + self.s[r1][c1]

matrix=[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]
NumMatrix.__init__(NumMatrix,matrix)
NumMatrix.sumRegion(NumMatrix,2,1,4,3)
NumMatrix.sumRegion(NumMatrix,1,1,2,2)
NumMatrix.sumRegion(NumMatrix,1,2,2,4)