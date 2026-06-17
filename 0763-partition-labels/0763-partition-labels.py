class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ct = Counter(s)
        res = []
        c = 0
        window = set()
        for i in range(len(s)):
            ct[s[i]] -= 1
            window.add(s[i])
            c += 1
            
            f = 1
            for l in window:
                if ct[l] != 0:
                    f = 0
                    break
            if f:
                res.append(c)
                c = 0
                window.clear()
        return res