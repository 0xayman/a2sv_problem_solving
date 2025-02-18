# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        cnt = 0

        for i in range(n):
            if i < n - 1 and nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

            if nums[i] != 0:
                nums[i], nums[cnt] = 0, nums[i]
                cnt += 1

        return nums
