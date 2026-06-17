class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        c1 = 0
        c2 = 0
        for i in bills:
            if i == 5:
                c1 += 1
            elif i == 10:
                if c1:
                    c1 -= 1
                    c2 += 1
                else:
                    return False
            else:
                if c2:
                    c2 -= 1
                    if c1:
                        c1 -= 1
                    else:
                        return False
                else:
                    if c1 > 2:
                        c1 -= 3
                    else:
                        return False
        return True
