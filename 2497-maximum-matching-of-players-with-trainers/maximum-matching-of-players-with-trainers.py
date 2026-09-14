class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort(), trainers.sort()
        m, n = len(players),len(trainers) 
        left, right = 0, 0
        count = 0

        while left < m and right < n:
            if players[left] <= trainers[right]:
                count += 1
                left += 1
            right += 1
        return count

        