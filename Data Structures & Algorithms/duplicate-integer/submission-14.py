class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        summary = set()
        for i in range(len(nums)):
            if nums[i] in summary:
                return True
            else:
                summary.add(nums[i])
        return False



            
