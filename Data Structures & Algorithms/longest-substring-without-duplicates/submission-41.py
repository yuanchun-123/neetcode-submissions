class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        seen = set()
        l, r = 0, 0
        while l <= r and r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            res = max(res, r-l+1)
            seen.add(s[r])
            r += 1
        return res
        

