class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        if n <= 1:
            return words

        dp = [words[0]]

        for i in range(1, n):
            if groups[i] != groups[i - 1]:
                dp.append(words[i])
        return dp