# https://leetcode.com/problems/max-increase-to-keep-city-skyline/description/
class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # Find max horizontal and vertical
        # Increase to the min of the two max
        row_max = [0] * len(grid)
        col_max = [0] * len(grid[0])
        for i in range(len(grid)):
            row_max[i] = max(grid[i])
        for j in range(len(grid[0])):
            for i in range(len(grid)):
                col_max[j] = max(col_max[j], grid[i][j])
        max_sum = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                max_sum += (min(row_max[i], col_max[j]) - grid[i][j])
        return max_sum
