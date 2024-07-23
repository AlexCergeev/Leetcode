class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        while l <= r:
            m = (l + r) // 2
            if matrix[m][0] < target:
                l = m + 1
            elif target <  matrix[m][0]:
                r = m - 1
            else:
                return True
        row = (l + r) // 2

        l, r = 0, len(matrix[row]) - 1
        while l <= r:
            m = (l + r) // 2
            if matrix[row][m] < target:
                l = m + 1
            elif target <  matrix[row][m]:
                r = m - 1
            else:
                return True
        return False
        