class Solution:
    def twoSum(self, num: List[int], target: int) -> List[int]:
        n = len(num)
        l, r = 0, n - 1
        while l < r:
            cur = num[l] + num[r]
            if cur > target:
                r -= 1
            elif cur < target:
                l += 1
            else: 
                return [l+1, r+1]
