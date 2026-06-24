class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        u, d = 0, len(matrix)-1
        while u <= d:
            mid = u + (d-u)//2
            if matrix[mid][0] <= target <= matrix[mid][len(matrix[0])-1]:
                l, r = 0, len(matrix[0])-1
                while l <= r:
                    col = l + (r-l)//2
                    if matrix[mid][col] == target:
                        return True
                    elif matrix[mid][col] > target:
                        r = col - 1
                    else:
                        l = col + 1
                return False
            elif matrix[mid][0] > target:
                d = mid - 1
            else:
                u = mid + 1
        return False