class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n,0) + 1
        freq = defaultdict(list)
        for num, f in count.items():
            freq[f].append(num)

        res = []
        for f in range(max(freq.keys()), 0, -1):
            for num in freq[f]:
                res.append(num)
                if len(res) == k:
                    return res

