class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        nums1 = nums[1:]
        nums2 = nums[:-1]
        memo1 = {}
        memo2 = {}
        def dp(i, numsi, memoi):
            if i >= len(numsi):
                return 0
            if i in memoi:
                return memoi[i]
            memoi[i] = max(dp(i+1, numsi, memoi), dp(i+2, numsi, memoi)+numsi[i])
            return memoi[i]
        return max(dp(0, nums1, memo1), dp(0, nums2, memo2))
            
            