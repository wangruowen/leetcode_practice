# https://leetcode.com/problems/triangle/description/
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if len(triangle) == 0: return 0
        if len(triangle) == 1: return triangle[0][0]

        # f[i][j] = triangle[i][j] + min(f[i + 1][j], f[i + 1][j + 1])
        f = list(triangle[-1])
        for i in xrange(2, len(triangle) + 1):
            for j in xrange(len(triangle[-i])):
                f[j] = triangle[-i][j] + min(f[j], f[j + 1])

        return f[0]
