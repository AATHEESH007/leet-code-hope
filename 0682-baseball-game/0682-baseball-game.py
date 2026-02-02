class Solution:
    def calPoints(self, op: List[str]) -> int:
        score = []
        for i in op:
            if i == 'C':
                score.pop()
            elif i == 'D':
                score.append(2*score[-1])
            elif i == '+':
                score.append(score[-1]+score[-2])
            else:
                score.append(int(i))
        print(score)
        return sum(score)