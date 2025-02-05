# Problem: Swap Case - https://www.hackerrank.com/challenges/swap-case?isFullScreen=true

def swap_case(s):
    newStr = ""
    for char in s:
        if char.isupper():
            newStr += char.lower()
        else:
            newStr += char.upper()
            
    return newStr
