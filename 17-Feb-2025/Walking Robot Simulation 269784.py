# Problem: Walking Robot Simulation - https://leetcode.com/problems/walking-robot-simulation/description/?envType=problem-list-v2&envId=array

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x, y = 0, 0
        # -2: Turn left 90 degrees.
        # -1: Turn right 90 degrees.
        
        # 0, 1 -> North (UP)
        # 1, 0 -> East (Right)
        # 0, -1 -> South (Down)
        # -1, 0 -> West  (Left)

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        current_dir = 0 # North (UP)
        obstacles=set(map(tuple,obstacles))

        max_distance = 0
    
        for command in commands:
            if command == -1:
                current_dir = (current_dir + 1) % 4
            elif command == -2:
                current_dir = (current_dir - 1) % 4
            else:
                for i in range(command):
                    new_x, new_y = x + directions[current_dir][0], y + directions[current_dir][1]

                    if (new_x, new_y) in obstacles:
                        break
                    
                    x, y = new_x, new_y
                    max_distance = max(max_distance, x*x + y*y)
        
        return max_distance

