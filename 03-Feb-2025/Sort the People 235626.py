# Problem: Sort the People - https://leetcode.com/problems/sort-the-people/

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        hashmap = {}
        for i in range(len(names)):
            hashmap[heights[i]] = names[i]

        heights.sort(reverse = True)
        ans = []
        for h in heights:
            ans.append(hashmap[h])
        
        return ans