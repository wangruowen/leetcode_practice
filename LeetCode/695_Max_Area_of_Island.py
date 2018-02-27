# https://leetcode.com/problems/max-area-of-island/description/
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.row_len, self.col_len = len(grid), len(grid[0])
        max_area = 0
        for i in range(self.row_len):
            for j in range(self.col_len):
                if grid[i][j] == 1:
                    max_area = max(max_area, self.dfs(i, j, grid))

        return max_area

    def dfs(self, i, j, grid):
        area = 0
        stack = [(i, j)]
        while len(stack) > 0:
            i, j = stack.pop()
            if grid[i][j] == 1:
                area += 1
                # Mark 0 as visited
                grid[i][j] = 0
            if i > 0 and grid[i - 1][j] == 1:
                stack.append((i - 1, j))
            if i < self.row_len - 1 and grid[i + 1][j] == 1:
                stack.append((i + 1, j))
            if j > 0 and grid[i][j - 1] == 1:
                stack.append((i, j - 1))
            if j < self.col_len - 1 and grid[i][j + 1] == 1:
                stack.append((i, j + 1))

        return area

grid=[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
s = Solution()
print(s.maxAreaOfIsland(grid))
