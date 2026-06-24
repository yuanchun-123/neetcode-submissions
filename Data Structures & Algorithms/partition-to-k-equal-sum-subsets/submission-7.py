class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        l = total // k
        nums.sort()
        if total%k != 0 or nums[-1]>l or len(nums)<k:
            return False
        s = [0]*k

        def dfs(i):
            if i == len(nums):
                return True
            seen = set()
            for j in range(k):
                if s[j] in seen:
                    continue
                seen.add(s[j])
                if s[j] + nums[i] <= l:
                    s[j] += nums[i]
                    if dfs(i+1):
                        return True
                    s[j] -= nums[i]
            return False
        return dfs(0)
                