class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}
        for i in range(len(nums)):
            need = target - nums[i]
            if need in count:
                return [count[need], i]
            count[nums[i]] = i
