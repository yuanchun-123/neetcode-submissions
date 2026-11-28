class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums or nums[0] > target or nums[-1] < target:
            return -1

        if nums[0] == target:
            return 0
        if nums[-1] == target:
            return len(nums) - 1
        
        l, r = 0, len(nums) - 1
        while l < r - 1:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m
            else:
                r = m
        return -1

        # l, r = 0, len(nums)-1
        
        # while l <= r:
        #     mid = l + (r-l)//2
        #     if nums[mid] == target:
        #         return mid
        #     elif nums[mid] < target:
        #         l = mid + 1
        #     else:
        #         r = mid - 1
        # return -1