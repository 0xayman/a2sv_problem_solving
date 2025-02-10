# Problem: 4Sum II - https://leetcode.com/problems/4sum-ii/

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        dict_1_2 = {}
        ans = 0
        for n1 in nums1:
            for n2 in nums2:
                dict_1_2[n1 + n2] = dict_1_2.get(n1 + n2, 0) + 1
        
        
        
        for n3 in nums3:
            for n4 in nums4:
                s = n3 + n4

                ans += dict_1_2.get(-s, 0)

        return ans