class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = n*[1]
        m = 1
        for i in range(1,n):
            if nums[i] > nums[i-1]:
                dp[i] = dp[i-1] + 1
            m = max(dp[i],m)
        return m