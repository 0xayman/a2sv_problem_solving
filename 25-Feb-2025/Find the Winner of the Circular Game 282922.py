# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution(object):
    def findTheWinner(self, n, k):
        l = list(range(n))
        count = n
        idx = 0
        while len(l)>1:
            if idx+k-1 > len(l)-1:
                idx = (idx + k - 1) % len(l)
            else:
                idx = idx + k - 1
            l.pop(idx)
#            idx += 1
        return l[0]+1






        