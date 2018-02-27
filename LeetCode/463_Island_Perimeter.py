# https://leetcode.com/problems/island-perimeter/description/
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.row_len, self.col_len = len(grid), len(grid[0])
        for i in range(self.row_len):
            for j in range(self.col_len):
                if grid[i][j] == 1:
                    return self.get_perimeter_by_dfs(i, j, grid)
        return 0


    def get_perimeter_by_dfs(self, i, j, grid):
        perimeter = 0
        stack = [(i, j)]
        while len(stack) > 0:
            i, j = stack.pop()
            if grid[i][j] == -1:
                continue
            grid[i][j] = -1  # Mark it visited
            init_peri = 4
            if i > 0:
                if grid[i - 1][j] == 1:
                    init_peri -= 1
                    stack.append((i - 1, j))
                elif grid[i - 1][j] == -1:
                    init_peri -= 1
            if i < self.row_len - 1:
                if grid[i + 1][j] == 1:
                    init_peri -= 1
                    stack.append((i + 1, j))
                elif grid[i + 1][j] == -1:
                    init_peri -= 1
            if j > 0:
                if grid[i][j - 1] == 1:
                    init_peri -= 1
                    stack.append((i, j - 1))
                elif grid[i][j - 1] == -1:
                    init_peri -= 1
            if j < self.col_len - 1:
                if grid[i][j + 1] == 1:
                    init_peri -= 1
                    stack.append((i, j + 1))
                elif grid[i][j + 1] == -1:
                    init_peri -= 1
            perimeter += init_peri

        return perimeter


s = Solution()
print(s.islandPerimeter([[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]))