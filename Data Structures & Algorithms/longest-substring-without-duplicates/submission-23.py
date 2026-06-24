class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        result = 0
        seen = set()

        while l in range(len(s)):
            for r in range(l, len(s)):
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
                seen.add(s[r])
                result = max(result, r - l + 1)
        return result







        

        