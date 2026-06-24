class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(i, cur, t):
            if t == target:
                res.append(cur.copy())
                return
            if i == len(nums) or t > target:
                return
            dfs(i+1, cur+[nums[i]], t+nums[i])
            while i+1<len(nums) and nums[i]==nums[i+1]:
                i += 1
            dfs(i+1, cur, t)
        dfs(0,[],0)
        return res