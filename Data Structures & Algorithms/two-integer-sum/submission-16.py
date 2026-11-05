class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapp = {}
        for i in range(len(nums)):
            need = target - nums[i]
            if nums[i] in mapp:
                return [mapp[nums[i]], i]
            else:
                mapp[need] = i