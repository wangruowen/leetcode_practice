# https://leetcode.com/problems/walls-and-gates/
class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        # BFS
        if not rooms:
            return

        INT_MAX = 2 ** 31 - 1
        row_len, col_len = len(rooms), len(rooms[0])
        def BFS(i, j):
            queue, dist, cur_min_dist = [[i, j]], 0, INT_MAX
            visited = set()
            while queue:
                new_queue = []
                dist += 1
                while queue:
                    i, j = queue.pop(0)
                    visited.add((i, j))
                    if dist >= cur_min_dist:
                        # If current exploring dist is already larger than
                        # the cur_min_dist we encounter previously with visited neighbors
                        return cur_min_dist
                    for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                        i_p, j_p = i + di, j + dj
                        if 0 <= i_p < row_len and 0 <= j_p < col_len and (i_p, j_p) not in visited:
                            if rooms[i_p][j_p] == 0:
                                return dist
                            elif rooms[i_p][j_p] == INT_MAX:
                                new_queue.append([i_p, j_p])
                            elif 0 < rooms[i_p][j_p] < INT_MAX:
                                cur_min_dist = min(cur_min_dist, rooms[i_p][j_p] + dist)
                queue = new_queue
            return cur_min_dist

        for i in range(row_len):
            for j in range(col_len):
                if rooms[i][j] == INT_MAX:
                    rooms[i][j] = BFS(i, j)


    def wallsAndGates_v2(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        # We should start from Gate 0 to get backwards to each point in the room
        INF = 2147483647
        row_len, col_len = len(rooms), len(rooms[0])
        q = [[i, j] for i in range(row_len) for j in range(col_len) if rooms[i][j] == 0]
        while q:
            i, j = q.pop(0)
            for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                i_p, j_p = i + di, j + dj
                if 0 <= i_p < row_len and 0 <= j_p < col_len and rooms[i][j] == INF:
                    rooms[i_p][j_p] = rooms[i][j] + 1
                    q.append([i_p, j_p])




s = Solution()
rooms = [[0,2147483647,-1,2147483647,2147483647,-1,-1,0,0,-1,2147483647,2147483647,0,-1,2147483647,2147483647,2147483647,2147483647,0,2147483647,0,-1,-1,-1,-1,2147483647,-1,-1,2147483647,2147483647,-1,-1,0,0,-1,0,0,0,2147483647,0,2147483647,-1,-1,0,-1,0,0,0,2147483647],[2147483647,0,-1,2147483647,0,-1,-1,-1,-1,0,0,2147483647,2147483647,-1,-1,2147483647,-1,-1,2147483647,2147483647,-1,0,-1,2147483647,0,2147483647,-1,2147483647,0,2147483647,0,2147483647,-1,2147483647,0,2147483647,-1,2147483647,0,2147483647,2147483647,0,-1,2147483647,-1,-1,-1,0,2147483647]]
print("before")
for i in range(len(rooms)):
    rooms_tmp = [x if x < 2147483647 else 'X' for x in rooms[i]]
    print(rooms_tmp)
s.wallsAndGates(rooms)
print("after")
for i in range(len(rooms)):
    rooms_tmp = [x if x < 2147483647 else 'X' for x in rooms[i]]
    print(rooms_tmp)