# https://leetcode.com/problems/keys-and-rooms/description/
class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        # BFS
        queue = [0]
        while len(queue) > 0:
            cur_key = queue.pop(0)
            if rooms[cur_key] == -1:
                continue
            for each_key in rooms[cur_key]:
                queue.append(each_key)
            rooms[cur_key] = -1 # Mark it visited
        for each_room in rooms:
            if each_room != -1:
                return False
        return True

