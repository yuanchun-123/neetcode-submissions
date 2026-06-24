class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        mapp = Counter(tasks)
        max_n = max(mapp.values())
        count_max = 0
        for value in mapp.values():
            if value == max_n:
                count_max += 1
        return max(len(tasks), (n+1) * (max_n - 1) + count_max)