# https://leetcode.com/problems/set-matrix-zeroes/description/
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0: return
        first_row = matrix[0]
        first_col = [row[0] for row in matrix]
        first_row_has_zero = True if 0 in first_row else False
        first_col_has_zero = True if 0 in first_col else False

        # Use first row and first column for book keeping
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[0])):
                if matrix[i][j] == 0:
                    first_col[i] = '#'
                    first_row[j] = '#'

        for i in xrange(1, len(matrix)):
            if first_col[i] == '#':
                for j in xrange(1, len(matrix[0])):
                    matrix[i][j] = 0
        for j in xrange(1, len(matrix[0])):
            if first_row[j] == '#':
                for i in xrange(1, len(matrix)):
                    matrix[i][j] = 0

        # Finally, change the book keeping to 0
        for j in xrange(len(first_row)):
            if first_row_has_zero or first_row[j] == '#':
                first_row[j] = 0
        for i in xrange(len(matrix)):
            if first_col_has_zero or first_col[i] == '#':
                matrix[i][0] = 0

