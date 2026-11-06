class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num,0) + 1
        
        freq = defaultdict(list)
        for num, f in count.items():
            freq[f].append(num)

        res = []
        for i in range(max(freq.keys()), 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

