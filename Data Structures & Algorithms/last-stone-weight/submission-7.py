class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones.sort()
        while (len(stones) >= 2):
            diff = abs(stones[-1] - stones[-2])
            stones.remove(stones[-1])
            stones.remove(stones[-1])
            if diff != 0:
                stones.append(diff)
                stones.sort()
        if not stones:
            return 0
        return stones[0]
