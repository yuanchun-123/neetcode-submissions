class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_vol = 0
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                vol = (j-i) * min(heights[i], heights[j])
                max_vol = max(max_vol, vol)
        return max_vol

        