# Problem: Keyboard Row - https://leetcode.com/problems/keyboard-row/description/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = "qwertyuiop"
        row2 = "asdfghjkl"
        row3 = "zxcvbnm"

        def isInRow(word, row):
            for char in word.lower():
                if char not in row:
                    return False
            
            return True

        ans = []
        for word in words:
            if isInRow(word, row1) or isInRow(word, row2) or isInRow(word, row3):
                ans.append(word)

        return ans