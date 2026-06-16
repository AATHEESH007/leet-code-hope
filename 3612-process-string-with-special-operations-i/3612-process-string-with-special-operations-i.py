def reverse(s):
    return s[::-1]
def remove(s):
    if s == '' or len(s) == 1:
        return ''
    return s[:-1]
def dup(s):
    return s+s
def add(s,x):
    return s+x
class Solution:
    def processStr(self, s: str) -> str:
        ans = ''
        for i in s:
            if i == '*':
                ans = remove(ans)
            elif i == '%':
                ans = reverse(ans)
            elif i == '#':
                ans = dup(ans)
            else:
                ans = add(ans,i)
        return ans