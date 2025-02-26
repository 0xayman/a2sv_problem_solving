# Problem: Maximum Sum of an Hourglass - LeetCode - https://leetcode.com/problems/maximum-sum-of-an-hourglass/description/

class Solution:
    def calc_sum(self, matrix, start_row, start_col):
        res = 0
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if (i == start_row + 1 and (j == start_col or j == start_col + 2)):
                    continue
                res += matrix[i][j]
        return res

    def maxSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        max_res = 0
        i = 0

        while (i + 2 < m):
            j = 0
            while (j + 2 < n):
                max_res = max(max_res, self.calc_sum(grid, i, j))
                j += 1
            i += 1
        return max_res