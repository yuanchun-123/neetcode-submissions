class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        n = len(nums)
        res = []

        for i in range(n):
            count[nums[i]] = count.get(nums[i], 0) + 1
            if count[nums[i]] > n // 3 and (nums[i] not in res):
                res.append(nums[i])
        return res