# Problem: Rotate Image - https://leetcode.com/problems/rotate-image/

import numpy as np
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        """
        rows = len(matrix)
        cols = len(matrix[0])
        for row in range(rows):
            for col in range(row+1, rows):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
        for row in range(rows):
            matrix[row].reverse()
            
