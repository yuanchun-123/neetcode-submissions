class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def back(i, cur, l):
            if cur == target:
                res.append(l.copy())
                return
            if i == len(nums) or cur > target:
                return
            
            back(i, cur+nums[i], l+[nums[i]])
            back(i+1, cur, l)

        back(0, 0, [])
        return res