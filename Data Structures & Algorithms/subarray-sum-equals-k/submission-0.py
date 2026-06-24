class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prex = 0
        count = {0:1}

        for num in nums:
            prex += num
            diff = prex - k
            res += count.get(diff, 0)
            count[prex] = count.get(prex, 0) + 1
        return res
