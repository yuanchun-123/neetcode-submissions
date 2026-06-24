class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            target = 0 - nums[i]
            res = set()
            j = i + 1
            while j < len(nums):
                need = target - nums[j]
                if need in res:
                    result.append([nums[i], nums[j], need])
                    j += 1
                    while j < len(nums) and nums[j] == nums[j-1]:
                        j +=1
                else:
                    res.add(nums[j])
                    j += 1
        return result

                    


