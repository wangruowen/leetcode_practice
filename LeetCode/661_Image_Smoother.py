# https://leetcode.com/problems/image-smoother/description/
class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        row_len, col_len = len(M), len(M[0])
        result = [[0 for _ in M[0]] for _ in M]
        for i in xrange(row_len):
            for j in xrange(col_len):
                cur_surrounds = []
                for di, dj in [(-1, -1), (-1, 0), (-1, 1),
                               (0, -1), (0, 0), (0, 1),
                               (1, -1), (1, 0), (1, 1)]:
                    if 0 <= i + di < row_len and 0 <= j + dj < col_len:
                        cur_surrounds.append(M[i + di][j + dj])
                result[i][j] = sum(cur_surrounds) / len(cur_surrounds)
        return result
