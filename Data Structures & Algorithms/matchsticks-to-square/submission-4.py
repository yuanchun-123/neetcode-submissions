class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        total = sum(nums)
        l = sum(nums)//4
        nums.sort(reverse=True)

        if len(nums) < 4 or total%4 != 0 or nums[0] > l:
            return False
        
        sides = [0]*4
        def dfs(i):
            if i == len(nums):
                return True
            for j in range(len(sides)):
                if sides[j] + nums[i] <= l:
                    sides[j] += nums[i]
                    if dfs(i+1):
                        return True
                    sides[j] -= nums[i]
                
                    
            return False
        return dfs(0)
        