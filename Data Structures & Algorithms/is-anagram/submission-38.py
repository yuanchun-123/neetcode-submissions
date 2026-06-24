class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        if m != n:
            return False
        count_m, count_n = {}, {}
        for i in range(m):
            count_m[s[i]] = count_m.get(s[i], 0) + 1
            count_n[t[i]] = count_n.get(t[i], 0) + 1
        return count_m == count_n
