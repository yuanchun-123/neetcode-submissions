class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        each = total // k
        nums.sort(reverse=True)
        if len(nums)<k or total%k != 0 or nums[0]>each:
            return False
        s = [0]*k

        def dfs(i):
            seen = set()
            if i == len(nums):
                return True
            for j in range(k):
                if s[j] in seen:
                    continue
                if s[j] + nums[i] <= each:
                    s[j] += nums[i]
                    if dfs(i+1):
                        return True
                    s[j] -= nums[i]
                    seen.add(s[j])
            return False
        return dfs(0)