# https://github.com/wangruowen/LeetCode-Solutions#bit-manipulation
from collections import defaultdict

class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [0]

        # Bottom Up Approach, Interesting thought
        # We approach the problem by starting from all leaf nodes
        # For example: given n = 6, edges = [[0, 3], [1, 3], [2, 3], [3, 4], [4, 5], [5, 6]]
        # All leaf nodes are 0, 1, 2, 6
        # We start from these four leaf nodes, their degree is one, take one step forward,
        # now 3, 5 are step 1, take one more step forward, now both merge to 4, which is step 2.
        # As a result, 4 is the root. The step 2 is also the min height value.
        neighbors = defaultdict(set)
        for a, b in edges:
            neighbors[a].add(b)
            neighbors[b].add(a)

        # Here, we assume all nodes are connected as a tree, we don't consider isolated forest
        degree_map = {k: len(v) for k, v in neighbors.items()}

        # Now we start from every leaf node
        leaf_nodes = [i for i in degree_map if degree_map[i] == 1]
        while n > 2:
            n -= len(leaf_nodes)
            new_leaf_nodes = []
            for leaf in leaf_nodes:
                for nei in neighbors[leaf]:
                    degree_map[nei] -= 1
                    if degree_map[nei] == 1:
                        new_leaf_nodes.append(nei)
            leaf_nodes = new_leaf_nodes

        # Either only one leaf, or two leaves connect to each other
        return leaf_nodes


s = Solution()
n = 7
edges = [[0,1],[1,2],[1,3],[2,4],[3,5],[4,6]]
print(s.findMinHeightTrees(n, edges))