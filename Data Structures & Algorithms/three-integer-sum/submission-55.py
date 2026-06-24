class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        count = {}
        nums.sort()
        for i in range(len(nums)):
            need = 0 - nums[i]
            count[need] = i
        for j in range(len(nums)):
            for k in range(j+1, len(nums)):
                cur = nums[j] + nums[k]
                if cur in count and count[cur] != j and count[cur] != k:
                    res.add(tuple(sorted([nums[count[cur]], nums[j], nums[k]])))
        return [list(x) for x in res]
        
