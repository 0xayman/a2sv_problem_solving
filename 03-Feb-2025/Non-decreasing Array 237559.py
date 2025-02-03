# Problem: Non-decreasing Array - https://leetcode.com/problems/non-decreasing-array/

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        counter = 0 
        n = len(nums)
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                counter += 1
                if counter > 1:
                    return False
                
                if i < 2 or nums[i - 2] <= nums[i]:
                    nums[i - 1] = nums[i] 
                else:
                    nums[i] = nums[i - 1] 
        
        return True