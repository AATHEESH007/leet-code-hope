class Solution:
    def possibleStringCount(self, word: str) -> int:
        c=0
        word=" "+word
        for i in range(len(word)):
            if word[i]==word[i-1]:
                c+=1
        return c+1
