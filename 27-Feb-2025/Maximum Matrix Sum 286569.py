# Problem: Maximum Matrix Sum - https://leetcode.com/problems/maximum-matrix-sum/description/?envType=problem-list-v2&envId=matrix

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        min_num = 10 ** 6
        summation = 0
        negatives = 0
        for row in matrix:
            for num in row:
                if (num < 0):
                    negatives += 1
                if (abs(num) < min_num):
                    summation += min_num if min_num != 10 ** 6 else 0
                    min_num = abs(num)
                else:
                    summation += abs(num)
        if negatives % 2:
            return summation - min_num
        return summation + min_num 