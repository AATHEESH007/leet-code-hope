class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        if colors[0] != colors[-1]: return len(colors) -1
        x = 0
        i = 0
        j = len(colors) - 1
        while True:
            if colors[i] != colors[j]:
                x = j
                break
            j -= 1
        j = len(colors) - 1
        i = 0
        while True:
            if colors[i] != colors[j]:
                if x < (j-i):
                    x = j - i
                break
            i += 1
        return x