# Problem: Remove Comments - https://leetcode.com/problems/remove-comments/

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        
        curr = ""
        comm = False
        result = []
        for line in source:
            i = 0
            n = len(line)
            while i < n:
                if comm:
                    if i < n-1 and line[i] == "*" and line[i+1] == "/":
                        comm = False
                        i += 1
                    
                else:
                    if i<n-1 and line[i] == "/" and line[i+1] == "/":
                        if curr != "":
                            result.append(curr)
                            curr = ""
                        break
                    elif i<n-1 and line[i] == "/" and line[i+1] == "*":
                        comm = True
                        i += 1
                        
                    else:
                        curr += line[i]
                i += 1
            
            if not comm and curr != "":
                result.append(curr)
                curr = ""
                
        return result
