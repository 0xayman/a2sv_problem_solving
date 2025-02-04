# Problem: Masking Personal Information - https://leetcode.com/problems/masking-personal-information/description/?envType=problem-list-v2&envId=string

class Solution:
    def maskPII(self, s: str) -> str:
        
        def isEmail(s):
            return s.count("@") > 0
        
        def maskEmail(s):
            s = s.lower()
            name = list(s.split("@")[0])
            domain = s.split("@")[1]
            name = name[0] + "*****" + name[-1]

            return "".join(name) + "@" + domain

        
        def maskPhone(s):
            phone_with_code = [char for char in s if char not in ["+", "-", "(", ")", " "]]
            phone = phone_with_code[-10:]
            code = "".join(phone_with_code[:-10])
            last_4 = "".join(phone[-4:] )

            code_mask = ["", "+*", "+**", "+***"][len(code)]
            phone_mask = "***-***"
            code_mask = code_mask + "-" if code_mask else code_mask
            return code_mask + phone_mask + "-" + last_4
        
        return maskEmail(s) if isEmail(s) else maskPhone(s)
