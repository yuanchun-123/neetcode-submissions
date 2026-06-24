class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:    
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            diff = heapq.heappop(stones) - heapq.heappop(stones)
            if diff != 0:
                heapq.heappush(stones, diff)
        return -stones[0] if stones else 0

