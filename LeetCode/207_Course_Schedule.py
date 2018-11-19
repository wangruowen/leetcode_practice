# https://leetcode.com/problems/course-schedule/
from collections import defaultdict

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # If cycle loop dependency found, then no
        # otherwise, just visit all
        depend_map = defaultdict(list)
        for k, v in prerequisites:
            depend_map[k].append(v)

        global_visited_cache = set()
        def DFS(course, visited=set()):
            nonlocal global_visited_cache
            if course in global_visited_cache:
                return True

            for each_pre in depend_map[course]:
                if each_pre in visited:
                    # Loop detected
                    return False

                visited.add(each_pre)
                if not DFS(each_pre, visited):
                    return False
                visited.remove(each_pre)

            global_visited_cache.add(course)
            return True

        # cached_visited = set()
        for i in range(numCourses):
            if not DFS(i):
                return False

        return True


s = Solution()
n = 8
courses = [[1,0],[2,6],[1,7],[6,4],[7,0],[0,5]]
print(s.canFinish(n, courses))