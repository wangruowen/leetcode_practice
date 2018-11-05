# https://leetcode.com/problems/search-a-2d-matrix/
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        # Start from Top Right
        row_len, col_len = len(matrix), len(matrix[0])

        i, j = 0, col_len - 1
        while i < row_len and j >= 0:
            if target == matrix[i][j]:
                return True
            elif target > matrix[i][j]:
                i += 1
            else:
                j -= 1
        return False

s = Solution()
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
target = 3
print(s.searchMatrix(matrix, target))