# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        rabbits = Counter(answers)
        total_rabbits = 0

        for x, freq in rabbits.items():
            group_size = x +  1
            required_groups = math.ceil(freq / group_size)

            total_rabbits += group_size * required_groups

        
        return total_rabbits

