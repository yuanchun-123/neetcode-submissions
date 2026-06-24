class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] < nums[r]:           # window already sorted
                return nums[l]
            m = (l + r) // 2
            if nums[m] > nums[r]:           # mid in left (rotated) half
                l = m + 1
            else:                            # mid in right (sorted) half
                r = m
        return nums[l]

