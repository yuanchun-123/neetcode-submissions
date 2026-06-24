class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = {0:1}
        prefix = 0
        res = 0
        for n in nums:
            prefix += n
            need = prefix - k
            res += count.get(need, 0)
            count[prefix] = count.get(prefix, 0) + 1
        return res
