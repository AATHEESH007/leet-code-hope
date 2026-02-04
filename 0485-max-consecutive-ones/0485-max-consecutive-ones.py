class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        c = 0
        for i in nums:
            if i == 1:
                c += 1
                ans = max(c,ans)
                print(c)
            else:
                c = 0
                print(c,ans)
        return ans