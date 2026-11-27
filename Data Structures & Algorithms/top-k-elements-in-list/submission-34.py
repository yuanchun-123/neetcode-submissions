class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        arr = []
        for n, c in count.items():
            arr.append([c, n])
        arr.sort()

        res = []
        while len(res) < k:
            cnt, num = arr.pop()
            res.append(num)
        
        return res
