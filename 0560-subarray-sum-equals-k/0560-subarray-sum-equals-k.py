class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        x = 0
        d = {0:1}
        c = 0
        for i in nums:
            x += i
            if (x-k) in d:
                c += d[x-k]
            d[x] = d.get(x,0) + 1
        return c