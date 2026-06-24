class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(m, n):
            tmp = nums[m]
            nums[m] = nums[n]
            nums[n] = tmp

        l, r, i = 0, len(nums) - 1, 0
        while i <= r:
            if nums[i] == 0:
                swap(l, i)
                i += 1
                l += 1
            elif nums[i] == 2:
                swap(r, i)
                r -= 1
            else:
                i += 1
        
