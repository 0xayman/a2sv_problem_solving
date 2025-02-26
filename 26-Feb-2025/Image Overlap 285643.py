# Problem: Image Overlap - https://leetcode.com/problems/image-overlap/description/

from collections import Counter
class Solution:
    def largestOverlap(self, img1, img2): 
        n = len(img1)
        h = []
        img1_ones = []
        img2_ones = []
        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    img1_ones.append((i, j))  
        for k in range(n):
            for l in range(n):
                if img2[k][l] == 1:
                    img2_ones.append((k, l))  
        for i in range(len(img1_ones)):
            for j in range(len(img2_ones)):
                x = img2_ones[j][0] - img1_ones[i][0]
                y = img2_ones[j][1] - img1_ones[i][1]
                h.append((x, y)) 
        h_counter = Counter(h)
        return max(h_counter.values(), default=0)