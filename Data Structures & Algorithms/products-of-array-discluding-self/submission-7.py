class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            pre, post = 1, 1
            j = 0
            while j < i:
                pre = pre * nums[j]
                j += 1
            for m in range(i+1, len(nums)):
                post = post * nums[m]
            mul = pre * post
            result.append(mul)
        return result


        