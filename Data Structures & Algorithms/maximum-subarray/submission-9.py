class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix = 0
        prefix_m = 0
        best = -float('inf')
        for n in nums:
            prefix += n
            best = max(best, prefix - prefix_m)
            prefix_m = min(prefix_m, prefix)
        return best