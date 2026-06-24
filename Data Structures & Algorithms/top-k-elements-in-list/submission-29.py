class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []
        for n in nums:
            count[n] = count.get(n, 0) + 1

        freq = defaultdict(list)

        for num, f in count.items():
            freq[f].append(num)
        
        for m in range(max(count.values()), 0, -1):
            for num in freq[m]:
                res.append(num)
                if len(res) == k:
                    return res
