class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ""
        for c in s:
            if ord('a') <= ord(c.lower()) <= ord('z') \
            or ord('0') <= ord(c.lower()) <= ord('9'):
                new += c.lower()
            else:
                continue
        l, r = 0, len(new)-1
        while l < r:
            if not new[l] == new[r]:
                return False
            l += 1
            r -= 1
        return True