class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, cur):
            if i == len(nums) or sum(cur) > target:
                if sum(cur) == target:
                    res.append(cur.copy())
                return
            exclude = dfs(i+1, cur)
            include = dfs(i, cur + [nums[i]])
        dfs(0, [])
        return res