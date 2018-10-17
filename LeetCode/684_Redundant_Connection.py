# https://leetcode.com/problems/redundant-connection/description/
from collections import defaultdict

class Solution:
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # Find the cycle or we can use Union-Find to solve
        adjacency_matrix = defaultdict(list)
        for u, v in edges:
            adjacency_matrix[u].append(v)
            adjacency_matrix[v].append(u)

        def DFS(i, visited_nodes, visited_edges=set()):
            if i not in adjacency_matrix:
                return None

            for j in adjacency_matrix[i]:
                cur_edge = (i, j) if i < j else (j, i)
                if cur_edge in visited_edges:
                    # Already visited this edge, skip
                    continue
                visited_edges.add(cur_edge)
                if j in visited_nodes:
                    # Reach already-visited node j from another edge
                    return visited_nodes[visited_nodes.index(j):]
                visited_nodes.append(j)
                found = DFS(j, visited_nodes, visited_edges)
                if found:
                    return found

                # Backtrack
                visited_edges.remove(cur_edge)
                visited_nodes.pop()
            return None

        for i in adjacency_matrix:
            found = DFS(i, [i])
            if found:
                # Found cycle
                # print(result)
                for u, v in edges[::-1]:
                    if u in found and v in found:
                        return [u, v]

        return None

s = Solution()
edges = [[3,4],[1,2],[2,4],[3,5],[2,5]]
print(s.findRedundantConnection(edges))
