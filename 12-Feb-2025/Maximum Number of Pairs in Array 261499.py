# Problem: Maximum Number of Pairs in Array - https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        pairs = 0
        length = len(nums)

        for key in freq.keys():
            pairs += freq[key] // 2

        left = length  - 2*pairs
        return [pairs, left]