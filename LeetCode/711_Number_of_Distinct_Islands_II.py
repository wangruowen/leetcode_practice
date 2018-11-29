# https://leetcode.com/problems/number-of-distinct-islands-ii/
class Solution:
    def numDistinctIslands2(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        def dfs(i, j, grid, island):
            if not (0 <= i < len(grid) and
                    0 <= j < len(grid[0]) and
                    grid[i][j] > 0):
                return False
            grid[i][j] = -1
            island.append((i, j))
            for di, dj in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                dfs(i + di, j + dj, grid, island)
            return True

        def normalize(island):
            # one shape becomes 8 shapes
            shapes = [[] for _ in range(8)]
            for x, y in island:
                rotation_and_reflections = [[x, y], [x, -y], [-x, y], [-x, -y],
                                            [y, x], [y, -x], [-y, x], [-y, -x]]
                for k in range(8):
                    shapes[k].append(rotation_and_reflections[k])
            for each_shape in shapes:
                each_shape.sort()
                x0, y0 = each_shape[0]
                for p in each_shape:
                    p[0] -= x0
                    p[1] -= y0
            return min(shapes)

        islands = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                island = []
                if dfs(i, j, grid, island):
                    islands.add(str(normalize(island)))
        return len(islands)
