class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapp = {}
        for i in range(len(nums)):
            need = target - nums[i]
            if need in mapp:
                return [mapp[need], i]
            mapp[nums[i]] = i
