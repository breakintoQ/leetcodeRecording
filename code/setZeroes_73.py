class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        columns = len(matrix[0])
        rows_to_zero = set()
        columns_to_zero = set()

        for i in range (rows):
            for j in range (columns):
                if matrix[i][j] ==0:
                    rows_to_zero.add(i)
                    columns_to_zero.add(j)

        for i in range(rows):
            for j in range(columns):
                if i in rows_to_zero or j in columns_to_zero:
                    matrix[i][j] = 0
