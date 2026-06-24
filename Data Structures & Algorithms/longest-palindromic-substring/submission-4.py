class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        if len(s) == 0:
            return res
        def dp(i):
            nonlocal res
            l, r = i, i
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    l -= 1
                    r += 1
                else:
                    break
            if (r-l-1) > len(res):
                res = s[l+1:r]
            l, r = i, i+1
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    l -= 1
                    r += 1
                else:
                    break
            if (r-l-1) > len(res):
                res = s[l+1:r]
        for j in range(len(s)):
            dp(j)
        return res
        