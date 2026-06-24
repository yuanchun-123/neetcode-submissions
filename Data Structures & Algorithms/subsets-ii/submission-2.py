class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        # 1. Organization: Sorting is mandatory to group duplicates
        nums.sort()
        
        def dfs(i, cur):
            # Base Case: Reached the end of the assets
            if i == len(nums):
                res.append(cur[:])
                return
            
            # Choice 1: INCLUDE the current number
            cur.append(nums[i])
            dfs(i + 1, cur)
            cur.pop() # Backtrack to keep the ledger clean
            
            # Choice 2: EXCLUDE the current number
            # Skip all subsequent identical numbers to avoid redundant audits
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            
            # FIXED: Move to the index immediately following the last duplicate
            dfs(i + 1, cur)
            
        dfs(0, [])
        return res