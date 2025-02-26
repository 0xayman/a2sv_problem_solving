# Problem: Number of Boomerangs - https://leetcode.com/problems/number-of-boomerangs/description/

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        n = 0
        for a,b in points:
            c = {}
            for x,y in points:
                i = (x-a)**2 + (y-b)**2
                if i in c:
                    n += 2*c[i]
                    c[i] += 1
                else:
                    c[i] = 1
        return n
