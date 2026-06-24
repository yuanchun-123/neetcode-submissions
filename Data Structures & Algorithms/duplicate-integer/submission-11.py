class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        summary = {}
        for i in range(len(nums)):
            if nums[i] in summary:
                return True
            else:
                summary[nums[i]] = 1
        return False


            
