import pprint


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        """
        m_i,j                               --> m_j,(n - 1 - i)
        m_j,(n - 1 - i)                     --> m_(n - 1 - i),(n - 1 - j)
        m_(n - 1 - i),(n - 1 - j)           --> m_(n - 1 - j),i
        m_(n - 1 - j),i                     --> m_i,j
        """
        n = len(matrix)
        for i in xrange(n):
            for j in xrange(i, n - 1 - i):  # Note that, for every i, we start the inner circle.
                """
                ------------
                |----------|
                ||--------||
                |||------|||
                |||      |||
                |||------|||
                ||--------||
                |----------|
                ------------
                """
                temp = matrix[i][j]
                matrix[i][j] = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
                matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
                matrix[j][n - 1 - i] = temp


s = Solution()
matrix = [
    [5, 1, 9, 11],
    [2, 4, 8, 10],
    [13, 3, 6, 7],
    [15, 14, 12, 16]
]
pp = pprint.PrettyPrinter(indent=1, width=20)
print("Before rotate:")
pp.pprint(matrix)
s.rotate(matrix)
print("After rotate:")
pp.pprint(matrix)
