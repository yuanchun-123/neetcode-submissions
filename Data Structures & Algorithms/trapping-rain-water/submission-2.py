class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l_max = [float('-inf')] * n
        r_max = [float('-inf')] * n
        res = 0

        l_max[0] = height[0]
        r_max[-1] = height[-1]

        for i in range(n):
            l_max[i] = max(height[i], l_max[i-1])
        for i in range(n-2, -1, -1):
            r_max[i] = max(height[i], r_max[i+1])
        
        for i in range(n):
            cur = min(l_max[i], r_max[i]) - height[i]
            res += cur
        return res
        