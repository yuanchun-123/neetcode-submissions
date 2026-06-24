class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, cur, t):
            if t == target:
                res.append(cur.copy())
                return
            if i == len(nums) or t > target:
                return
            dfs(i+1, cur, t)
            dfs(i, cur+[nums[i]], t+nums[i])
        dfs(0, [], 0)
        return res

            