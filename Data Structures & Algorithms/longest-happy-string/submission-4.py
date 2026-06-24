class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ""
        h = []
        for cha, freq in [('a', a), ('b', b), ('c', c)]:
            if freq != 0:
                heapq.heappush(h, (-freq, cha))
        
        while h:
            freq, cha = heapq.heappop(h)
            if len(res)>1 and res[-1]==res[-2]==cha:
                if not h:
                    break
                next_freq, next_cha = heapq.heappop(h)
                res += next_cha
                next_freq += 1
                if next_freq != 0:
                    heapq.heappush(h, (next_freq, next_cha))
            else:
                res += cha
                freq += 1
            if freq != 0:
                heapq.heappush(h, (freq, cha))

        return res
        

        