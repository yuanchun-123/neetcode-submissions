class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        max_count = 0
        for num in nums:
            count[num] = count.get(num, 0) + 1
            if count[num] > max_count:
                max_count = count[num]
                res = num
        return res
        