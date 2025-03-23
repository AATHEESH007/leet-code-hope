class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        c=0
        x=max(nums)
        for i in range(len(nums)):
            if nums[i]==val:
                c+=1
                nums[i]=x+1
        nums.sort()
        return len(nums)-c