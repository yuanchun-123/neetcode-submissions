class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] <= nums[r]:         # window already sorted
                res = min(res, nums[l])
                break
            m = (l + r) // 2
            
            if nums[m] >= nums[l]:         # mid in left (higher) half
                l = m + 1                  # go right
            else:                          # mid in right (lower) half
                r = m                  # go left

            res = min(res, nums[m])        # keep running min
        return res

