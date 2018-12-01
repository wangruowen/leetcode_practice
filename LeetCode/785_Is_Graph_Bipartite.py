# https://leetcode.com/problems/is-graph-bipartite/
from collections import defaultdict

class Solution:
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        # Two groups, each group connect to the other but not it self
        # If a -> b, then a in 1st group, b in 2nd group
        # if b -> c, then b in 2nd group, c in 1st group
        # if c -> a, WRONG, a and c should not be in the same group
        neighbors = defaultdict(list)
        for i in range(len(graph)):
            for j in graph[i]:
                neighbors[i].append(j)
                neighbors[j].append(i)

        group1, group2, visited = set(), set(), set()
        def DFS(i, i_in_group1):
            nonlocal group1, group2

            for j in neighbors[i]:
                if i_in_group1:
                    if j in group1:
                        return False
                    elif j not in group2:
                        group2.add(j)
                        visited.add(j)
                        if not DFS(j, not i_in_group1):
                            return False
                else:
                    if j in group2:
                        return False
                    elif j not in group1:
                        group1.add(j)
                        visited.add(j)
                        if not DFS(j, not i_in_group1):
                            return False
            return True

        for i in range(len(graph)):
            if i not in visited:
                group1.add(i)
                if not DFS(i, True):
                    return False

        return True


s = Solution()
g = [[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]
print(s.isBipartite(g))