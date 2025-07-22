class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        sum = 0
        res = 0
        s = set()
        l = 0
        for i in range(len(nums)):
            while nums[i] in s:
                s.remove(nums[l])
                sum -= nums[l]
                l += 1
            s.add(nums[i])
            sum += nums[i]
            res = max(sum,res)
        return res