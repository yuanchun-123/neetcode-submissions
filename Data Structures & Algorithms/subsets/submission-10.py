class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(i, curr):
            if i == len(nums):
                res.append(curr.copy())
                return
            include = dfs(i+1, curr + [nums[i]])
            exclude = dfs(i+1, curr)
        dfs(0, [])
        return res
            