class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r, c = len(matrix), len(matrix[0])
        l, r = 0, r*c - 1
        while l <= r:
            mid = l + (r-l)//2
            if matrix[mid//c][mid%c] == target:
                return True
            elif matrix[mid//c][mid%c] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False