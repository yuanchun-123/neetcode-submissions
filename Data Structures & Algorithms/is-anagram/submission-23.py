class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss = list(s)
        ss.sort()
        ts = list(t)
        ts.sort()
        print(ss, ts)
        return ss == ts





