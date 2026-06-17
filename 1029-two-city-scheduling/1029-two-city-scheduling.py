class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        asum = sum((a for a,b in costs))
        diffs = sorted((x[1] - x[0]) for x in costs)
        for i in range(len(diffs)//2):
            asum += diffs[i]
        return asum 