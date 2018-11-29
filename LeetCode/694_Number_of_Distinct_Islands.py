# https://leetcode.com/problems/number-of-distinct-islands/
class Solution:
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # The shape should be the same
        # Maybe use top left as (0, 0)
        row_len, col_len = len(grid), len(grid[0])
        def DFS(i, j, points):
            points.append((i, j))
            for di, dj in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                ip, jp = i + di, j + dj
                if 0 <= ip < row_len and 0 <= jp < col_len and grid[ip][jp] == 1:
                    grid[ip][jp] = -1
                    # We need to set to -1 here to avoid child node in the queue
                    # to explore other already-in-queue nodes
                    DFS(ip, jp, points)

        def get_shape(points):
            # Find top left
            points.sort(key=lambda x: (x[0], x[1]))
            x0, y0 = points[0]
            shape_key = tuple([(x - x0, y - y0) for x, y in points])
            return shape_key

        shapes = set()
        for i in range(row_len):
            for j in range(col_len):
                if grid[i][j] == 1:
                    grid[i][j] = -1
                    point_set = []
                    DFS(i, j, point_set)
                    cur_shape = get_shape(point_set)
                    if cur_shape not in shapes:
                        shapes.add(cur_shape)
        return len(shapes)