# Problem: Row With Maximum Ones - https://leetcode.com/problems/row-with-maximum-ones/

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        matrix = [0, 0]
        for i in range(len(mat)):
            if mat[i].count(1) > matrix[1]:
                matrix[1] = mat[i].count(1)
                matrix[0] = i
        return matrix
