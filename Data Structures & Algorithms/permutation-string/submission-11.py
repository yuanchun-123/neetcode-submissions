class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2) 
        if m > n:
            return False

        count = {}
        want = {}
        for i in range(m):
            count[s2[i]] = count.get(s2[i],0) + 1
            want[s1[i]] = want.get(s1[i],0) + 1

        for i in range(n-m):
            if want == count:
                return True

            count[s2[i]] -= 1
            if count[s2[i]] == 0:
                del count[s2[i]]
            
            count[s2[i+m]] = count.get(s2[i+m],0) + 1
        return count == want
            



        