class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix, prefix_m = 0, 0
        best = -float('inf')
        for n in nums:
            prefix += n
            best = max(best, prefix - prefix_m)
            prefix_m = min(prefix, prefix_m)
        return best
