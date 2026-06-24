class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        half = sum(stones) // 2
        memo = {}
        def dp(i, cur):
            if cur > half:
                return -float('inf')
            if cur == half or i == len(stones):
                return cur
            key = (i, cur)
            if key in memo:
                return memo[key]
            memo[key] = max(dp(i+1, cur), dp(i+1, cur+stones[i]))
            return memo[key]
        return sum(stones) - 2 * dp(0, 0)