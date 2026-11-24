class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def back(i, cur):
            if i == len(nums):
                res.append(cur.copy())
                return
            back(i+1, cur + [nums[i]])
            back(i+1, cur)
        
        back(0, [])
        return res