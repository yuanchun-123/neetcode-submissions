class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 1
        count = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[l]:
                nums[l+1] = nums[r]
                count += 1
                l += 1
            
        return l + 1
