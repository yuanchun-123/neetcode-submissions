class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        res = []

        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1

        for num, ct in count.items():
            freq[ct].append(num)

        for j in range(len(freq)-1, 0, -1):
            for n in freq[j]:
                res.append(n)
                if len(res) == k:
                    return res



        


