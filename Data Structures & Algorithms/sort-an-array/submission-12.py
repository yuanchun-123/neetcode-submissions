class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(L, R):
            res = []
            i, j = 0, 0
            while i < len(L) and j < len(R):
                if L[i] <= R[j]:
                    res.append(L[i])
                    i += 1
                else:
                    res.append(R[j])
                    j += 1
            while i < len(L):
                res.append(L[i])
                i += 1
            while j < len(R):
                res.append(R[j])
                j += 1
            return res


        def mergesort(arr, l, r):
            if l >= r:
                return [arr[l]]
            m = (l + r) // 2
            left = mergesort(arr, l, m)
            right = mergesort(arr, m + 1, r)
            return merge(left, right)
        
        return mergesort(nums, 0, len(nums)-1)

