class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        h = []
        max_count = 0

        for i, task in enumerate(tasks):
            count[task] = count.get(task, 0) + 1
        
        for task, freq in count.items():
            h.append([-freq, task])
        heapq.heapify(h)

        freq, task = h[0]
        while h and freq == h[0][0]:
            freq, task = heapq.heappop(h)
            max_count += 1

        return max(max_count + (n+1)*(-freq-1) , len(tasks))

