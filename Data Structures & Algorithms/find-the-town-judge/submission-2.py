class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        scores = [0] * n
        for t in trust:
            scores[t[0]-1] -= 1
            scores[t[1]-1] += 1
        
        for i in range(len(scores)):
            if scores[i] == n - 1:
                return i+1
        return -1
