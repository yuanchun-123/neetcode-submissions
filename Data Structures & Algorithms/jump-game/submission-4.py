class Solution:
    def canJump(self, nums: List[int]) -> bool:
        h = 0
        for i in range(len(nums)):
            if i > h:
                break
            h = max(h, i+nums[i])
            if h >= len(nums) - 1:
                return True
        return False


