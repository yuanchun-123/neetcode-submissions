class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        maxi = 0
        while l < r:
            width = r - l
            cur = min(heights[l], heights[r]) * width
            maxi = max(maxi, cur)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return maxi

