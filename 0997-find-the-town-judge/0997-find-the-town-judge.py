class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusting = [0] * (n+1)
        trusted = [0] * (n+1)
        
        for i,j in trust:

            trusting[i] += 1

            trusted[j] += 1

        for i in range(1,len(trusting)):
            if trusting[i] == 0:
                if trusted[i] == n-1:
                    return i
        return -1