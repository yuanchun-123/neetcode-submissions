class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            seen = set()
            j = i + 1
            while j < n:
                need = -nums[i] - nums[j]
                if need in seen:
                    res.append([nums[i], need, nums[j]])
                    j += 1
                    # skip duplicate nums[j]
                    while j < n and nums[j] == nums[j-1]:
                        j += 1
                else:
                    seen.add(nums[j])
                    j += 1
        return res

                    


