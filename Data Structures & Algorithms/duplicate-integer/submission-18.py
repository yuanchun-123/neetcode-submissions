class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False

        dup = {}
        for i in range(len(nums)):
            dup[nums[i]] = dup.get(nums[i],0) + 1
            if dup[nums[i]] > 1:
                return True
        return False
        

        



            
