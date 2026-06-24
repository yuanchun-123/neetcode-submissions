class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dis = []
        res = []
        for i in range(len(points)):
            x, y = points[i]
            l = x ** 2 + y ** 2
            dis.append([l, x, y])
        
        heapq.heapify(dis)
        while k > 0:
            l, x, y = heapq.heappop(dis)
            res.append([x, y])
            k -= 1
        return res
        



