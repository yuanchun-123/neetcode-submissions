class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        h = []
        for num, start, end in trips:
            h.append([start, num])
            h.append([end, -num])
        heapq.heapify(h)

        curr_loc = 0
        curr_num = 0
        while h:
            loc, num = heapq.heappop(h)
            
            curr_num += num
            if curr_num > capacity:
                return False
            
        return True
        