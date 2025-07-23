class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def solve(pattern , s , score):
            stk = []
            point = 0
            for i in s:
                if stk and stk[-1] == pattern[0] and i == pattern[1]:
                    stk.pop()
                    point += score
                else:
                    stk.append(i)
            return point, "".join(stk)
        if x >= y:
            ans1 , S = solve('ab' , s , x)
            ans2 , S = solve('ba' , S , y)
        else:
            ans1 , S = solve('ba' , s , y)
            ans2 , S = solve('ab' , S , x)
        return ans1 + ans2