class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stk = []
        for i in range(len(num)):
            
            while stk  and k>0 and num[i]< stk[-1]:
                stk.pop()
                k -= 1
                
            
            stk.append(num[i])

        while k>0:
            stk.pop()
            k-=1
        ans=''.join(stk).lstrip('0')
        return ans if ans else "0"