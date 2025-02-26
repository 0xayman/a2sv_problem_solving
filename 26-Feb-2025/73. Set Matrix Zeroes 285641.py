# Problem: 73. Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/description/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        row0 = any(matrix[0][j] == 0 for j in range(len(matrix[0])))
        col0 = any(matrix[i][0] == 0 for i in range(rows))
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0], matrix[0][j] =  0, 0
        
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        if row0:
            for x in range(cols):
                matrix[0][x] = 0
        if col0:
            for k in range(rows):
                matrix[k][0] = 0