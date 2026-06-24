class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(i, cur):
            if i == len(nums):
                res.append(cur.copy())
                return
            include = dfs(i+1, cur+[nums[i]])
            exclude = dfs(i+1, cur)
        dfs(0, [])
        return res
