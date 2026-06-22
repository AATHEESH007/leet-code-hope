class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        ct = {'b':0,'a':0,'o':0,'l':0,'n':0}
        for i in text:
            if i in 'baloon':
                if i not in ct:
                    ct[i] = 1
                else:
                    ct[i] += 1
        ans = float('inf')
        print(ct)
        ct['o'] = ct['o'] // 2
        ct['l'] = ct['l'] // 2
        print(ct)

        for i in ct:
            if ans > ct[i]:
                ans = ct[i]
        return ans
        