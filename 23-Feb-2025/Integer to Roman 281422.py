# Problem: Integer to Roman - https://leetcode.com/problems/integer-to-roman/description/

   n = len(str(num))-1
        res = ""
        while num > 0:
            d = 10**(n)
            k = num//d 
            if k >= 5:
                if k == 9:
                    res += roman[9*d]
                else:
                    res += roman[5*d] + roman[d]*(k-5)
            else:
                if k == 4:
                    res += roman[4*d]
                else:
                    res += roman[d] * k

            num %= d
            n -= 1
        return res
