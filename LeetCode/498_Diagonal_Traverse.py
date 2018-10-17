# https://leetcode.com/problems/diagonal-traverse/description/
class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []

        # whenever hit edge then move to right next
        UP, DOWN = 0, 1
        row_len, col_len = len(matrix), len(matrix[0])
        i, j = 0, 0
        result = []
        direction = UP
        while i < row_len and j < col_len:
            result.append(matrix[i][j])
            if direction == UP:
                if i == 0:
                    j += 1
                    if j == col_len:
                        j -= 1
                        i += 1
                    direction = DOWN
                elif j == col_len - 1:
                    i += 1
                    direction = DOWN
                else:
                    i -= 1
                    j += 1
            else:
                if i == row_len - 1:
                    j += 1
                    direction = UP
                elif j == 0:
                    i += 1
                    if i == row_len:
                        i -= 1
                        j += 1
                    direction = UP
                else:
                    i += 1
                    j -= 1
        return result

s = Solution()
matrix = \
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
print(s.findDiagonalOrder(matrix))
