# https://leetcode.com/problems/redundant-connection/description/
from collections import defaultdict

class Solution:
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # Find the cycle
        adjacency_matrix = defaultdict(list)
        for u, v in edges:
            adjacency_matrix[u].append(v)

        def DFS(i, matrix, visited_edges, dup):
            if i not in matrix:
                return

            for j in matrix[i]:
                if j in result:
                    dup.append(j)
                    return
                    visited_edges.append(j)
                DFS(j, matrix, visited_edges, dup)

        for i in adjacency_matrix:
            result, dup = [], []
            DFS(i, adjacency_matrix, result, dup)
            if len(dup) > 0:
                # Found cycle
                # print(result)
                for u, v in edges[::-1]:
                    if u in result and v in result:
                        return [u, v]

        return None

s = Solution()
edges = [[3,4],[1,2],[2,4],[3,5],[2,5]]
print(s.findRedundantConnection(edges))
