class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums or nums[0] >= target:
            return 0
        if nums[-1] < target:
            return len(nums)
        if nums[-1] == target:
            return len(nums)-1

        l, r = 0, len(nums)-1
        while l < r-1:
            m = (l+r)//2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m
            else:
                l = m
        return r
        
        

