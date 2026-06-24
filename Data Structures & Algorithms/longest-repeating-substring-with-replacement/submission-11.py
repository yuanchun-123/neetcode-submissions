class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        count = {}
        max_f = 0 # Track the highest frequency found in the current window
        
        for r in range(len(s)):
            # 1. Update the ledger with the new character
            count[s[r]] = count.get(s[r], 0) + 1
            max_f = max(max_f, count[s[r]])
            
            # 2. Audit: Is the window valid? 
            # (Window Length - Frequency of most common char) must be <= k
            while (r - l + 1) - max_f > k:
                # 3. If invalid, shrink from the left
                count[s[l]] -= 1
                l += 1
            
            # 4. Record the best valid window found
            res = max(res, r - l + 1)
            
        return res