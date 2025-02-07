# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses/

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        results = {}
        for match in matches:
            winner, loser = match[0], match[1]

            results[winner] = results.get(winner, 0)
            results[loser] = results.get(loser, 0) + 1

        zero_lost = []
        one_lost = []
        print(results)
        for player, loses in results.items():
            if loses == 0:
                zero_lost.append(player)
            
            if loses == 1:
                one_lost.append(player)

        zero_lost.sort()
        one_lost.sort()

        return [zero_lost, one_lost]