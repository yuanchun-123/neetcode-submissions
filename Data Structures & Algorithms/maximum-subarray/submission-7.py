class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix = 0
        best = -float('inf')
        min_prefix = 0
        
        for n in nums:
            prefix += n
            best = max(best, prefix - min_prefix)
            min_prefix = min(min_prefix, prefix)
        return best