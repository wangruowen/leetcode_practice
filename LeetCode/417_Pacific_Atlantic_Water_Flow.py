# https://leetcode.com/problems/pacific-atlantic-water-flow/
class Solution:
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix:
            return []
        # DFS find points can be reached by both top-left and bottom-right boundaries
        row_len, col_len = len(matrix), len(matrix[0])
        pacific_visited, atlantic_visited = set(), set()

        def DFS(i, j, visited):
            for di, dj in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                ip, jp = i + di, j + dj
                if 0 <= ip < row_len and 0 <= jp < col_len \
                        and (ip, jp) not in visited \
                        and matrix[i][j] <= matrix[ip][jp]:
                    visited.add((ip, jp))
                    DFS(ip, jp, visited)

        # From pacific
        for j in range(col_len):
            if (0, j) not in pacific_visited:
                pacific_visited.add((0, j))
                DFS(0, j, pacific_visited)
        for i in range(row_len):
            if (i, 0) not in pacific_visited:
                pacific_visited.add((i, 0))
                DFS(i, 0, pacific_visited)

        # From atlantic
        for j in range(col_len):
            i = row_len - 1
            if (i, j) not in atlantic_visited:
                atlantic_visited.add((i, j))
                DFS(i, j, atlantic_visited)
        for i in range(row_len):
            j = col_len - 1
            if (i, j) not in atlantic_visited:
                atlantic_visited.add((i, j))
                DFS(i, j, atlantic_visited)

        return list(pacific_visited.intersection(atlantic_visited))
