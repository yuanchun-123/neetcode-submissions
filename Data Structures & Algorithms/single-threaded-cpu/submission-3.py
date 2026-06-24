class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        res, waiting = [], []
        tasks = [[e, p, i] for i, [e, p] in enumerate(tasks)]
        tasks.sort(key = lambda x: x[0])
        time = tasks[0][0]
        n, i = len(tasks), 0

        while len(res) < n:
            while i < n and tasks[i][0] <= time:
                heapq.heappush(waiting, (tasks[i][1], tasks[i][2]))
                i += 1
            if not waiting:
                time = tasks[i][0]
            else:
                proc, idx = heapq.heappop(waiting)
                time += proc
                res.append(idx)
        return res



        