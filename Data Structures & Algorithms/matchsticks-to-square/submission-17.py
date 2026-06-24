class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        t = sum(nums)
        l = t // 4
        nums.sort(reverse=True)
        if t % 4 != 0 or nums[0] > l or len(nums) < 4:
            return False

        s = [0] * 4
        def dfs(i):
            if i == len(nums):
                return True
            for j in range(4):
                if s[j] + nums[i] <= l:
                    s[j] += nums[i]
                    if dfs(i+1):
                        return True
                    s[j] -= nums[i]
            return False
        return dfs(0)
                    
        