# Problem: Find Words That Can Be Formed by Characters - https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        characters = {}
        for char in chars:
            characters[char] = chars.count(char)

        print(characters)
        res = 0
        for word in words:
            is_good = True
            for char in word:
                if word.count(char) > characters.get(char, 0):
                    is_good = False
                    break
            
            if is_good:
                res += len(word)

        return res
