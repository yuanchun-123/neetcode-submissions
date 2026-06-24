class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = [[] for _ in range(len(nums)+1)]
        res = []
        mapping = {}
        for num in nums:
            mapping[num] = mapping.get(num, 0) + 1

        for key, value in mapping.items():
            count[value].append(key)

        for i in range(len(nums), 0, -1): 
            if count[i]:
                for n in count[i]:
                    res.append(n)
                if len(res) == k:
                    break
        return res

        


