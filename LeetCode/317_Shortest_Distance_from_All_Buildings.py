# https://leetcode.com/problems/shortest-distance-from-all-buildings/
from collections import defaultdict

class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # BFS
        # In one round of BFS, Start from every building to take one step forward
        # until one node is all reached by n buildings
        row_len, col_len = len(grid), len(grid[0])
        buildings = [(i, j) for i in range(row_len) for j in range(col_len) if grid[i][j] == 1]
        build_num = len(buildings)
        empty_nodes = set([(i, j) for i in range(row_len) for j in range(col_len) if grid[i][j] == 0])
        nodes_covered_by_buildings = {}
        visited_by_building = {i: {each_pos} for i, each_pos in enumerate(buildings)}
        building_cover_nodes = {i: [each_pos] for i, each_pos in enumerate(buildings)}
        step = 0
        while True:
            step += 1
            all_new_points = []
            for build_id, cur_points in building_cover_nodes.items():
                new_points = []
                for i, j in cur_points:
                    for di, dj in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                        i_p, j_p = i + di, j + dj
                        if 0 <= i_p < row_len and 0 <= j_p < col_len and \
                                (i_p, j_p) not in visited_by_building[build_id] and (i_p, j_p) in empty_nodes:
                            new_points.append((i_p, j_p))
                            visited_by_building[build_id].add((i_p, j_p))
                            build_count = nodes_covered_by_buildings.get((i_p, j_p), defaultdict(int))
                            build_count[build_id] = step
                            nodes_covered_by_buildings[(i_p, j_p)] = build_count

                building_cover_nodes[build_id] = new_points
                all_new_points.extend(new_points)

            if not all_new_points:
                break

        shortest = float('inf')
        for point in empty_nodes:
            if point in nodes_covered_by_buildings and len(nodes_covered_by_buildings[point]) == build_num:
                # print(nodes_covered_by_buildings[point])
                # This point has been reached by all buildings
                shortest = min(shortest, sum(nodes_covered_by_buildings[point].values()))
        if shortest != float('inf'):
            return shortest
        else:
            return -1


s = Solution()
grid = [[1,1,1,1,1,1,1,0],[0,0,0,0,0,0,0,1],[1,1,1,1,1,1,0,1],[1,0,0,0,0,1,0,1],[1,0,1,1,0,1,0,1],[1,0,1,0,0,1,0,1],[1,0,1,1,1,1,0,1],[1,0,0,0,0,0,0,1],[0,1,1,1,1,1,1,0]]
print(s.shortestDistance(grid))

