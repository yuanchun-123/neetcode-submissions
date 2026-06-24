class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for i in range(len(nums)):
            seen[nums[i]] = seen.get(nums[i],0) + 1
            if seen[nums[i]] > 1:
                return True
        return False


        



            
