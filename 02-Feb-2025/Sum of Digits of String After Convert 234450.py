# Problem: Sum of Digits of String After Convert - https://leetcode.com/problems/sum-of-digits-of-string-after-convert/description/

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        hashmap = {}
        for idx, letter in enumerate(ascii_lowercase):
            hashmap[letter] = idx + 1
        
        str_to_num = []
        for char in s:
            str_to_num.append(str(hashmap[char]))

        str_to_num = "".join(str_to_num)
        
        ans = str_to_num
        for i in range(k):
            sub = 0
            for char in ans:
                sub += int(char)
            
            ans = str(sub)
        
        return int(ans)