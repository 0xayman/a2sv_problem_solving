# Problem: Roman to Integer - https://leetcode.com/problems/roman-to-integer/?envType=problem-list-v2&envId=string

class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        hashmap = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        i = 0
        while i < len(s):
            if i + 1 < len(s) and s[i] == "I" and s[i + 1] == "V":
                to_add = 4
                i += 2
            elif i + 1 < len(s) and s[i] == "I" and s[i + 1] == "X":
                to_add = 9
                i += 2
            elif i + 1 < len(s) and s[i] == "X" and s[i + 1] == "L":
                to_add = 40
                i += 2
            elif i + 1 < len(s) and s[i] == "X" and s[i + 1] == "C":
                to_add = 90
                i += 2
            elif i + 1 < len(s) and s[i] == "C" and s[i + 1] == "D":
                to_add = 400
                i += 2
            elif i + 1 < len(s) and s[i] == "C" and s[i + 1] == "M":
                to_add = 900
                i += 2
            else:
                to_add = hashmap[s[i]]
                i += 1
            num += to_add

        return num