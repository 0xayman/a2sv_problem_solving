# Problem: Find the Number of Distinct Colors Among the Balls - https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/description/

class Solution(object):
    def queryResults(self, limit, queries):
        colors = {}
        balls = {}
        ans = []
        for i in range(len(queries)):
            if queries[i][0] in balls:
                k = balls[queries[i][0]]
                if colors[k] ==1:
                    colors.pop(k)
                else:
                    colors[k] -= 1
            colors[queries[i][1]] = colors.get(queries[i][1], 0) + 1
            balls[queries[i][0]] = queries[i][1]

            ans.append(len(colors))
        return ans