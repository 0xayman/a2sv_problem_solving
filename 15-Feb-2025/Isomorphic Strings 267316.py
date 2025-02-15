# Problem: Isomorphic Strings - https://leetcode.com/problems/isomorphic-strings/

class Solution:
 def isIsomorphic(self, s: str, t: str) -> bool:
        char_dict = {}
        mapped_chars = set()

        if (len(t) != len(s)):
            return False
        
        for i in range(len(t)):
            if char_dict.get(s[i], None) == t[i]:
                continue
            
            if (char_dict.get(s[i], None) or t[i] in mapped_chars):
                return False

            char_dict[s[i]] = t[i]
            mapped_chars.add(t[i])
            
        return True