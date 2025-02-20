# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows, cols = len(mat), len(mat[0])
        res = []

        i, j = 0, 0

        for _ in range(rows * cols):
            res.append(mat[i][j])

            if (i + j) % 2 == 0:
                if j == cols - 1: # right bound
                    i += 1
                elif i == 0: # top bound
                    j += 1
                else: # diagonal up right
                    i -= 1
                    j += 1
            else:
                if i == rows - 1: # bottom bound
                    j += 1
                elif j == 0: # left bound
                    i += 1
                else: # diagonal down left
                    i += 1
                    j -= 1

        return res