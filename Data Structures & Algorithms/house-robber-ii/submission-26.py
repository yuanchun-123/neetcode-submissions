class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        nums1 = nums[1:]
        nums2 = nums[:-1]
        dp1 = [0] * (len(nums1) + 2)
        dp2 = [0] * (len(nums2) + 2)

        for i in range(len(nums1)-1, -1, -1):
            dp1[i] = max(dp1[i+2]+nums1[i], dp1[i+1])
            dp2[i] = max(dp2[i+2]+nums2[i], dp2[i+1])
        return max(dp1[0], dp2[0])
