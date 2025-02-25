# Problem: Longest Consecutive Sequence - https://leetcode.com/problems/longest-consecutive-sequence/description/

class Solution(object):
    def longestConsecutive(self, nums):
        if len(nums)==0:
            return 0
        nums = sorted(nums)
        ans = []
        x = 1
        for i in range(len(nums)-1):
            if nums[i]+1 == nums[i+1]:
                x += 1
            elif nums[i] == nums[i+1]:
                pass
            else:
                ans.append(x)
                x = 1
        ans.append(x)
        return max(ans) 

        
        