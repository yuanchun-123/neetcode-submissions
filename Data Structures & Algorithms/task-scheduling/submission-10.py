class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        max_freq = max(count.values())

        count_max = 0
        for task, freq in count.items():
            if freq == max_freq:
                count_max += 1
        
        return max(len(tasks), (max_freq-1)*(n+1)+count_max)

