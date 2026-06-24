class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        had = {}
        for i in range(len(nums)):
            need = target - nums[i]
            if need in had:
                return [had[need],i]
            else:
                had[nums[i]] = i