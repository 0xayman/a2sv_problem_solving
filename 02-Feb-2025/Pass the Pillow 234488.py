# Problem: Pass the Pillow - https://leetcode.com/problems/pass-the-pillow/description/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        chunks = time // (n - 1)
        even_ans = time % (n - 1) + 1
        odd_ans = n - time % (n - 1)
    
        return even_ans if chunks%2 == 0 else odd_ans