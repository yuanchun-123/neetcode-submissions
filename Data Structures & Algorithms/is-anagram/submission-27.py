class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)
        if not m == n:
            return False
        
        m_count = {}
        n_count = {}
        for i in range(m):
            m_count[s[i]] = m_count.get(s[i],0) + 1
            n_count[t[i]] = n_count.get(t[i],0) + 1
        
        return m_count == n_count







