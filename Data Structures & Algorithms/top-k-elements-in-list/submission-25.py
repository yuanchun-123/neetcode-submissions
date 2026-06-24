class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []
        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1
        
        freq = [[] for x in range(len(nums) + 1)]
        for key, value in count.items():
            freq[value].append(key)
            
        for m in range(len(nums), 0, -1):
            for num in freq[m]:
                res.append(num)
            if len(res) == k:
                return res
