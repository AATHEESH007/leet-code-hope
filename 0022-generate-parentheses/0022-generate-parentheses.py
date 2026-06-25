class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def start(open,close,s):
            if open == n and close == n:
                res.append(s)
                return
            
            if open < n:
                start(open + 1, close, s + "(")

            if close < open:
                start(open, close + 1, s + ")")
            return
        start(0,0,"")
        return res