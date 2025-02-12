# Problem: Replace Elements in an Array - https://leetcode.com/problems/replace-elements-in-an-array/

class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        indexes = {}
        for i in range(len(nums)):
            indexes[nums[i]] = i

        print(indexes)
        for i in range(len(operations)):
            old_num = operations[i][0]
            new_num = operations[i][1]

            old_num_idx = indexes[old_num]
            indexes[new_num] = old_num_idx
            nums[old_num_idx] = new_num


        return nums