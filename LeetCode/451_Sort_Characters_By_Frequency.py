# https://leetcode.com/problems/sort-characters-by-frequency/description/
from Queue import PriorityQueue

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        queue = PriorityQueue()
        visited = set()
        for c in s:
            if c in visited:
                continue
            else:
                queue.put((-s.count(c), c))
                visited.add(c)
        while not queue.empty():
            node = queue.get()
            result += node[1] * -node[0]
            print(node)
        return result

s = Solution()
print(s.frequencySort("tree"))
