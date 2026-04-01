class Solution:
    def maxRepeating(self, s: str, w: str) -> int:
        l1 = len(s)
        l2 = len(w)
        
        dp = [0] * (l1 + 1)
        
        for i in range(l2 - 1, l1):
            if s[i - l2 + 1 : i + 1] == w:
                dp[i + 1] = dp[i + 1 - l2] + 1
        
        return max(dp)