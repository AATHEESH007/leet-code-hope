class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        p = sorted(players)
        t = sorted(trainers)
        c = 0
        j = i = 0
        while i < len(p) and j < len(t):
            if p[i] <= t[j]:
                c += 1
                j += 1
                i += 1
            else:
                j += 1
        return c