class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        res = []

        for point in points:
            x, y = point
            dis = x**2 + y**2
            h.append((dis, point))
        heapq.heapify(h)

        while k > 0:
            dis, point = heapq.heappop(h)
            k -= 1
            res.append(point)

        return res


        



