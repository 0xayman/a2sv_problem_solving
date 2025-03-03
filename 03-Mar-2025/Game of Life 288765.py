# Problem: Game of Life - https://leetcode.com/problems/game-of-life/description/

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
        b2 = [[0] * m for i in range(n)]
        for i in range(n):
            for j in range(m):
                count = 0
                for k in range(max(i - 1, 0), min(i + 2, n)):
                    for l in range(max(j - 1, 0), min(j + 2, m)):
                        if i == k and j == l:
                            continue
                        count += board[k][l]
                if board[i][j] == 1 and count in [2, 3]:
                    b2[i][j] = 1
                elif board[i][j] == 0 and count == 3:
                    b2[i][j] = 1
        for i in range(n):
            for j in range(m):
                board[i][j] = b2[i][j]
        