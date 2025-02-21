# Problem: Flipping an Image - https://leetcode.com/problems/flipping-an-image/description/

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        
        for i in range(rows):
            image[i] = image[i][::-1] # [1, 1, 0] -> [0, 1, 1]
            for j in range(cols):
                image[i][j] = int(image[i][j] != 1)

        return image