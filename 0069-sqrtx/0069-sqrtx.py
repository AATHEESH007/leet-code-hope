class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        first, last = 1, x
        while first <= last:
            m= first + (last - first) // 2
            if m== x // m:
                return m
            elif m> x // m:
                last = m- 1
            else:
                first = m+ 1
        return last