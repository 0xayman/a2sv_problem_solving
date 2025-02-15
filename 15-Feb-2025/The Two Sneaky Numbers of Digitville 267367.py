# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        duplicates = []
        n = len(nums)

        for i in range(len(nums)):
            nums[i] += 1

        for x in nums:
            x = abs(x)
            
            if nums[x - 1] < 0:
                duplicates.append(x - 1)
            
            nums[x - 1] *= -1
        
        return duplicates