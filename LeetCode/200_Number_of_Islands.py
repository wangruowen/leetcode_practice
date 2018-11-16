# https://leetcode.com/problems/number-of-islands/
class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # DFS
        result = 0
        row_len, col_len = len(grid), len(grid[0])
        def DFS(i, j):
            if grid[i][j] == "1":
                grid[i][j] = "-1"
                for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    if 0 <= i + di < row_len and 0 <= j + dj < col_len:
                        DFS(i+di, j+dj)

        for i in range(row_len):
            for j in range(col_len):
                if grid[i][j] == "1":
                    result += 1
                    DFS(i, j)

        return result

s = Solution()
grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
print(s.numIslands(grid))