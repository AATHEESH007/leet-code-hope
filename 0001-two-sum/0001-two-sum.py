class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map={}
        for i,x in enumerate(nums):
            need = target - x
            if need in map:
                return [map[need],i]
            map[x] = i