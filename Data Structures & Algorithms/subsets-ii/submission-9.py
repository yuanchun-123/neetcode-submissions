class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def dfs(i, cur):
            if i == len(nums):
                res.append(cur.copy())
                return
            include = dfs(i + 1, cur + [nums[i]])
            while i + 1 < len(nums) and nums[i]==nums[i+1]:
                i += 1
            exclude = dfs(i + 1, cur)
        dfs(0, [])

        return res