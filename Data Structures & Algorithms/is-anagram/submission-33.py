class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1

        for r in t:
            count[r] = count.get(r, 0) - 1
        
        for key,value in count.items():
            if value != 0:
                return False
        return True






