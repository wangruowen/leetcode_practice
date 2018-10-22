# https://leetcode.com/problems/the-skyline-problem/description/
import heapq

class Solution(object):
    def getSkyline_has_memory_issue(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(buildings) == 0:
            return []
        # sort by Left index
        buildings.sort(key=lambda x: (x[0], x[1]))
        mleft, mright = buildings[0][0], buildings[-1][1]
        height_map = [0] * (mright - mleft)
        result = []
        for left, right, height in buildings:
            for i in range(left - mleft, right - mleft):
                height_map[i] = max(height_map[i], height)
        # print(height_map)
        last_h = None
        for i, h in enumerate(height_map):
            if i == 0 or last_h != h:
                result.append([i + mleft, h])
            last_h = h

        result.append([mright, 0])
        return result

    def getSkyline(self, buildings):
        if len(buildings) == 0:
            return []
        # sort by Left first, right second
        buildings.sort(key=lambda x: (x[0], x[1]))
        height_map = []
        for left, right, height in buildings:
            height_map.append([left, -height])  # Start
            height_map.append([right, height])  # End

        heapq.heapify()


s = Solution()
builds = [[0,2147483647,2147483647]]
print(s.getSkyline(builds))