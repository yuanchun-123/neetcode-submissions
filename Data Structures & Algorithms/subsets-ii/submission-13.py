class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def back(i, cur):
            if i >= len(nums):
                res.append(cur.copy())
                return 

            back(i+1, cur + [nums[i]])
            j = i + 1
            while j < len(nums) and nums[j] == nums[i]:
                j += 1
                
            back(j, cur)
        back(0, [])
        return res