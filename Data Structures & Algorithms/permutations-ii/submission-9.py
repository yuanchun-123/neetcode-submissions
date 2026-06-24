class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        seen = set()
        nums.sort()
        def dfs(i):
            if i == len(nums):
                if tuple(nums) in seen:
                    return
                res.append(nums.copy())
                seen.add(tuple(nums))
                return
            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                dfs(i+1)
                nums[i], nums[j] = nums[j], nums[i]
        dfs(0)
        return res

