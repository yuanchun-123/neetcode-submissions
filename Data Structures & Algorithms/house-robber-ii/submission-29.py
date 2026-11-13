class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        memo1, memo2 = {}, {}
        nums1 = nums[1:]
        nums2 = nums[:-1]
    
        def dfs(arr, memo, i):
            if i >= len(arr):
                return 0
            if i in memo:
                return memo[i]
            memo[i] = max(dfs(arr, memo, i+2) + arr[i], \
                        dfs(arr, memo, i+1))
            return memo[i]
        
        return max(dfs(nums1, memo1, 0), dfs(nums2, memo2, 0))