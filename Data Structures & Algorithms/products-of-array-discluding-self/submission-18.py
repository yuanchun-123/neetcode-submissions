class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        pre = [0]* len(nums)
        post = [0]* len(nums)

        pre[0] = 1
        for i in range(1, len(nums)):
            pre[i] = nums[i-1] * pre[i-1]

        post[len(nums)-1] = 1
        for j in range(len(nums)-2, -1, -1):
            post[j] = nums[j+1] * post[j+1]
            

        for i in range(len(nums)):
            result[i] = pre[i] * post[i]
        return result
        



        