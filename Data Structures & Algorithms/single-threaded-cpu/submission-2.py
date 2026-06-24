class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        res, waiting = [], []
        n = len(tasks)
        tasks = [[e, p, i] for i, (e, p) in enumerate(tasks)]
        tasks.sort(key = lambda x: x[0])
        time = tasks[0][0]

        i = 0
        while len(res) < n:
            while i < n and time >= tasks[i][0]:
                heapq.heappush(waiting, (tasks[i][1], tasks[i][2]))
                i += 1
            if not waiting:
                time = tasks[i][0]
            else:
                pro, idx = heapq.heappop(waiting)
                res.append(idx)
                time += pro
        return res



        