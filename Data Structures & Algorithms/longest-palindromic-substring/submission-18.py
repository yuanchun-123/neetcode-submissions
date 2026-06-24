class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        length = 0
        for i in range(len(s)):
            l, r = i, i
            while 0 <= l <= r < len(s):
                if s[l] != s[r]:
                    break
                l -= 1
                r += 1
            if r - l - 1 > length:
                length = r - l - 1
                res = s[l+1:r]
        
            l, r = i, i + 1
            while 0 <= l <= r < len(s):
                if s[l] != s[r]:
                    break
                l -= 1
                r += 1
            if r - l - 1 > length:
                length = r - l - 1
                res = s[l+1:r]
        return res
        