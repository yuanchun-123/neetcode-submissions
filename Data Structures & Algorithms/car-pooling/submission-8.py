class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        h = []
        trips.sort(key=lambda x: x[1])
        count = 0

        for num, start, end in trips:
            while h and h[0][0] <= start:
                old_end, old_num = heapq.heappop(h)
                count -= old_num

            heapq.heappush(h, (end, num))
            count += num

            if count > capacity:
                return False
        return True