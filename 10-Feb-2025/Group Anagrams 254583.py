# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = defaultdict(list)

        for s in strs:
            sorted_s = sorted(s)
            anagrams[str(sorted_s)].append(s)

        return [word for word in anagrams.values()]