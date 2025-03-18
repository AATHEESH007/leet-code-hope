class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s       
        ML=1
        Ma=s[0]
        for i in range(len(s)-1):
            for j in range(i+1,len(s)):
                if j-i+1 > ML and s[i:j+1] == s[i:j+1][::-1]:
                    ML = j-i+1
                    Ma = s[i:j+1]
        return Ma