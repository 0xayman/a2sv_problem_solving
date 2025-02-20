# Problem: Image Smoother - https://leetcode.com/problems/image-smoother/description/

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows, cols = len(img), len(img[0])
        result = [[0 for i in range(cols)] for j in range(rows)]

        for i in range(rows):
            for j in range(cols):
                total, count = 0, 0

                for x in range(i - 1, i + 2):
                    for y in range(j - 1, j + 2):
                        if 0 <= x < rows and 0 <= y < cols:
                            total += img[x][y]
                            count += 1


                result[i][j] = total // count

        return result