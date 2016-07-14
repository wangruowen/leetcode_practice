# https://leetcode.com/problems/minimum-path-sum/

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        LEFT, DOWN = 1, 2
        m, n = len(grid), len(grid[0])
        min_so_far = [[0 for i in xrange(n)] for j in xrange(m)]
        min_path = [[0 for i in xrange(n)] for j in xrange(m)]
        for i in xrange(m - 1, -1, -1):
            for j in xrange(n - 1, -1, -1):
                if i == m - 1 and j == n - 1:
                    min_so_far[i][j] = grid[i][j]
                else:
                    if i == m - 1:
                        min_so_far[i][j] = min_so_far[i][j + 1] + grid[i][j]
                        min_path[i][j] = LEFT
                    elif j == n - 1:
                        min_so_far[i][j] = min_so_far[i + 1][j] + grid[i][j]
                        min_path[i][j] = DOWN
                    else:
                        if min_so_far[i + 1][j] >= min_so_far[i][j + 1]:
                            min_so_far[i][j] = min_so_far[i][j + 1] + grid[i][j]
                            min_path[i][j] = LEFT
                        else:
                            min_so_far[i][j] = min_so_far[i + 1][j] + grid[i][j]
                            min_path[i][j] = DOWN

        return min_so_far[0][0]

