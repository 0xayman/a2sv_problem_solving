# Problem: Majority Element II (Optional) - https://leetcode.com/problems/majority-element-ii/

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        counter = Counter(nums)

        ans = []

        for key in counter:
            if counter[key] > n / 3:
                ans.append(key)

        return ans