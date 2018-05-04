# https://leetcode.com/problems/toeplitz-matrix/description/
class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        # Diagonal: (i, j) -> (i + 1, j + 1)
        row_len, col_len = len(matrix), len(matrix[0])
        for i in xrange(row_len):
            cur_val = matrix[i][0]
            cur_i, cur_j = i + 1, 1
            while cur_i < row_len and cur_j < col_len:
                if cur_val != matrix[cur_i][cur_j]:
                    return False
                cur_i += 1
                cur_j += 1

        for j in xrange(1, col_len):
            cur_val = matrix[0][j]
            cur_i, cur_j = 1, j + 1
            while cur_i < row_len and cur_j < col_len:
                if cur_val != matrix[cur_i][cur_j]:
                    return False
                cur_i += 1
                cur_j += 1

        return True
