# https://leetcode.com/problems/swim-in-rising-water/description/
from queue import PriorityQueue

class Solution:
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # Priority Queue is better than DFS in this case
        n = len(grid)
        queue = PriorityQueue()
        queue.put((grid[0][0], (0, 0)))
        visited = set([(0, 0)])
        max_t = 0
        while True:
            item = queue.get()
            x, y = item[1]
            max_t = max(max_t, item[0])
            if x == n - 1 and y == n - 1:
                return max_t
            for dx, dy in [[-1,0],[1,0],[0,-1],[0,1]]:
                if 0 <= x + dx < n and 0 <= y + dy < n and (x+dx,y+dy) not in visited:
                    visited.add((x+dx,y+dy))
                    queue.put((grid[x+dx][y+dy], (x+dx,y+dy)))


s = Solution()
grid = [[7,11,5,3],[2,14,12,8],[4,13,9,10],[6,0,1,15]]
print(s.swimInWater(grid))