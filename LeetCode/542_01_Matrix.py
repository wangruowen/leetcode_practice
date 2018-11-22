# https://leetcode.com/problems/01-matrix/
class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        # BFS
        # Start from zeroes to find surround 1s, then continue with those 1s, to find further 1s
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return matrix
        row_len, col_len = len(matrix), len(matrix[0])
        queue = [(i, j) for i in range(row_len) for j in range(col_len) if matrix[i][j] == 0]
        visited = set(queue)
        while queue:
            new_queue = []
            for i, j in queue:
                for di, dj in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                    ip, jp = i + di, j + dj
                    if 0 <= ip < row_len and 0 <= jp < col_len and (ip, jp) not in visited:
                        new_queue.append((ip, jp))
                        visited.add((ip, jp))
                        if matrix[ip][jp] != 0:
                            matrix[ip][jp] = matrix[i][j] + 1
            queue = new_queue
        return matrix