class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        # We use l < r because when l == r, we have found the minimum
        while l < r:
            # 1. Early Exit: If the range is already sorted, the left is min
            if nums[l] < nums[r]:
                return nums[l]
                
            mid = l + (r - l) // 2
            
            # 2. Pivot Detection: Compare mid with the right boundary
            if nums[mid] > nums[r]:
                # The minimum must be in the right half (excluding mid)
                l = mid + 1
            else:
                # The minimum is either at mid or to its left
                r = mid
                
        return nums[l]