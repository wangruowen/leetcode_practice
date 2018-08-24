# https://leetcode.com/problems/trapping-rain-water-ii/description/
import heapq

class Solution:
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if len(heightMap) == 0:
            return 0

        row_len, col_len = len(heightMap), len(heightMap[0])
        queue, visited = [], set()
        # First, add borders to the queue
        for i in range(row_len):
            heapq.heappush(queue, (heightMap[i][0], [i, 0]))
            visited.add((i, 0))
            heapq.heappush(queue, (heightMap[i][col_len - 1], [i, col_len - 1]))
            visited.add((i, col_len - 1))
        for j in range(1, col_len - 1):
            heapq.heappush(queue, (heightMap[0][j], [0, j]))
            visited.add((0, j))
            heapq.heappush(queue, (heightMap[row_len - 1][j], [row_len - 1, j]))
            visited.add((row_len - 1, j))

        result = 0
        # heapq + BFS
        while len(queue) > 0:
            cur_lowest, cur_pos = heapq.heappop(queue)
            cur_i, cur_j = cur_pos
            for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                new_i, new_j = cur_i + di, cur_j + dj
                if 0 <= new_i < row_len and 0 <= new_j < col_len \
                        and (new_i, new_j) not in visited:
                    if cur_lowest > heightMap[new_i][new_j]:
                        result += cur_lowest - heightMap[new_i][new_j]
                    visited.add((new_i, new_j))
                    heapq.heappush(queue, (max(heightMap[new_i][new_j], cur_lowest), [new_i, new_j]))
        return result

