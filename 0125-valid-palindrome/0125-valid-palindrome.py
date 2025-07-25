class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans = ""
        ans2 = ""
        for i in s:
            if i.isalnum():
                i = i.lower()
                ans = i + ans
                ans2 = ans2 + i
        print(ans, ans2)
        if ans == ans2:
            return True
        else:
            return False