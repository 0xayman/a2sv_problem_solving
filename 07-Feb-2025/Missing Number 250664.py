# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        seq_sum = n * (n + 1) // 2
        actual_sum = sum(nums)

        return seq_sum - actual_sum 