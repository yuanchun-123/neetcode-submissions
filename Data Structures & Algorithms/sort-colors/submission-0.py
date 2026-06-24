class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def merge(arr, L, M, R):
            left = arr[L: M+1]
            right = arr[M+1: R+1]
            i, j, k = 0, 0, L
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    nums[k] = left[i]
                    i += 1
                else:
                    nums[k] = right[j]
                    j += 1
                k += 1
            while i < len(left):
                nums[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                nums[k] = right[j]
                j += 1
                k += 1

        def mergesort(arr, l, r):
            if l >= r:
                return arr
            m = (l + r) // 2
            mergesort(arr, l, m)
            mergesort(arr, m + 1, r)
            merge(arr, l, m, r)

        mergesort(nums, 0, len(nums))
        