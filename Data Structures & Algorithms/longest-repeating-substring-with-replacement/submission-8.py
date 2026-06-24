class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        count = {}
        res = 0
        freq = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            freq = max(freq, count[s[r]])

            if (r - l + 1) - freq > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, (r-l+1))
        return res




            

            

            
