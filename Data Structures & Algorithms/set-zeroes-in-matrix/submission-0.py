class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        rows, cols = len(matrix), len(matrix[0])
        new_rows, new_cols = [False] * rows, [False] * cols

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    new_rows[r] = True
                    new_cols[c] = True

        for r in range(rows):
            for c in range(cols):
                if new_rows[r] == True or new_cols[c] == True:
                    matrix[r][c] = 0

        

