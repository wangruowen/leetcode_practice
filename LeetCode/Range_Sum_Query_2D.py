# https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            self.total = 0
        else:
            self.total = [[0 for i in range(0, len(matrix[0]) + 1)] for j in range(0, len(matrix) + 1)]
            for i in range(1, len(matrix) + 1):
                for j in range(1, len(matrix[0]) + 1):
                    self.total[i][j] = self.total[i - 1][j]
                    self.total[i][j] += self.total[i][j - 1]
                    self.total[i][j] += matrix[i - 1][j - 1]
                    self.total[i][j] -= self.total[i - 1][j - 1]
            print(self.total)

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.total[row2 + 1][col2 + 1] - self.total[row2 + 1][col1] - self.total[row1][col2 + 1] + self.total[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
matrix = [[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]
numMatrix = NumMatrix(matrix)
print numMatrix.sumRegion(2,1,4,3)
print numMatrix.sumRegion(1,1,2,2)
print numMatrix.sumRegion(1,2,2,4)

