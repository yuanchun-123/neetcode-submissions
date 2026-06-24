class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        for point in points:
            x, y = point
            dis = x**2 + y**2
            heapq.heappush(h, (-dis, point))

        while len(h) > k:
            heapq.heappop(h)

        res = []
        for dis, point in h:
            res.append(point)
        return res


        



