class Solution:
    def mirrorDistance(self, n: int) -> int:
        x = n
        a = 0
        while x>0:
            r = x%10
            x = x//10
            a = a*10 + r
        if n > a:
            return n - a
        return a - n