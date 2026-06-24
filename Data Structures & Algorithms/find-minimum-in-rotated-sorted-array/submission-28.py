class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        res = nums[0]
        while l <= r:
            mid = l + (r-l)//2
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
                
            if nums[mid] <= nums[r]:
                r = mid - 1
                res = min(res, nums[mid])
            elif nums[mid] >= nums[l]:
                l = mid + 1
                res = min(res, nums[r])
        return res
            

       
