class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, L, M, R):
            left = arr[L: M + 1]
            right = arr[M + 1: R + 1]
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
                return [arr]
            m = (l + r) // 2
            left = mergesort(arr, l, m)
            right = mergesort(arr, m + 1, r)
            return merge(arr, l, m, r)

        mergesort(nums, 0, len(nums) - 1)
        return nums


