# https://leetcode.com/problems/graph-valid-tree/
from collections import defaultdict

class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        # Tree has n-1 edges and connect all n nodes
        # Need to meet two rules
        # 1. all nodes can be reached from any node
        # 2. No loop
        if len(edges) != n - 1:
            # Tree must have n - 1 edges
            return False

        neighbor_map = defaultdict(set)
        for k, v in edges:
            neighbor_map[k].add(v)
            neighbor_map[v].add(k)

        # BFS
        # For a tree, if we start from 0, eventually, we should reach all nodes
        def BFS():
            queue = [0]
            visited = set()
            while queue:
                cur = queue.pop(0)
                visited.add(cur)
                for each_nei in neighbor_map[cur]:
                    if each_nei not in visited:
                        queue.append(each_nei)

            return len(visited) == n

        # DFS
        def DFS():
            stack, visited = [0], set()
            while stack:
                cur = stack.pop()
                visited.add(cur)
                for each_nei in neighbor_map[cur]:
                    if each_nei not in visited:
                        stack.append(each_nei)
            return len(visited) == n

        def UnionFind():
            pass

        return BFS() or DFS()




s = Solution()
n = 5
edges = [[0,1],[0,4],[1,4],[2,3]]
# edges = [[0,1],[0,2],[0,3],[1,4]]
print(s.validTree(n, edges))