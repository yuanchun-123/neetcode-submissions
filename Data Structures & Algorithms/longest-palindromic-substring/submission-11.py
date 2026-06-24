class Solution:
    def longestPalindrome(self, s: str) -> str:
        k = 0
        res = ''
        for i in range(len(s)):
            l, r = i, i
            while 0<=l<len(s) and 0<=r<len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if r-l-1 > k:
                k = r - l - 1
                res = s[l+1:r]
            l, r = i, i + 1
            while 0<=l<len(s) and 0<=r<len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if r-l-1 > k:
                k = r - l - 1
                res = s[l+1:r]
        
        return res
