# Problem: Rearrange Array Elements by Sign - https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans = [0 for i in range(len(nums))]
        next_pos = 0
        next_neg = 1
        for num in nums:
            if num > 0:
                ans[next_pos] = num
                next_pos += 2
            else:
                ans[next_neg] = num
                next_neg += 2

        return ans