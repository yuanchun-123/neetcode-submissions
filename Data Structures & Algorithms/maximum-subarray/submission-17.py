class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix = 0
        m_pre = 0
        res = -float('inf')
        for n in nums:
            prefix += n
            res = max(prefix-m_pre, res)
            m_pre = min(m_pre, prefix)
        return res