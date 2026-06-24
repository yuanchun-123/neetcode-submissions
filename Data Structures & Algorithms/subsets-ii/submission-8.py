class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        def dfs(i, cur):
            if i == len(nums):
                res.add(tuple(cur.copy()))
                return
            include = dfs(i + 1, cur + [nums[i]])
            while i + 1 < len(nums) and nums[i]==nums[i+1]:
                i += 1
            exclude = dfs(i + 1, cur)
        dfs(0, [])
        res = list(res)
        for i in range(len(res)):
            res[i] = list(res[i])
        return res