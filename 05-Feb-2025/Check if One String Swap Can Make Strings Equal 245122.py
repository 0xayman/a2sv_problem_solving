# Problem: Check if One String Swap Can Make Strings Equal - https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/description/

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        def_pos = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                def_pos.append(i)

        if len(def_pos) != 0 and len(def_pos) != 2:
            return False

        if len(def_pos) == 0:
            return True
        
        if s1[def_pos[0]] == s2[def_pos[1]] and s1[def_pos[1]] == s2[def_pos[0]]:
            return True
        
        return False