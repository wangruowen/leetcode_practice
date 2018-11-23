# https://leetcode.com/problems/closest-leaf-in-a-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque, defaultdict

class Solution:
    def findClosestLeaf(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # BFS
        # Transform back to a graph, with neighbor map,
        # Start from the k node, stop at the first encountered leaf
        neighbors = defaultdict(set)
        q = deque([root])
        k_node = None
        while q:
            cur = q.popleft()
            if cur.val == k:
                k_node = cur

            # Add an attribute for is leaf or not
            if not cur.left and not cur.right:
                cur.is_leaf = True
            else:
                cur.is_leaf = False

            if cur.left:
                neighbors[cur].add(cur.left)
                neighbors[cur.left].add(cur)
                q.append(cur.left)
            if cur.right:
                neighbors[cur].add(cur.right)
                neighbors[cur.right].add(cur)
                q.append(cur.right)

        q, visited = deque([k_node]), set([k_node])

        while q:
            new_q = deque()
            while q:
                cur = q.popleft()
                if cur.is_leaf:
                    return cur.val
                for nei in neighbors[cur]:
                    if nei not in visited:
                        visited.add(nei)
                        new_q.append(nei)
            q = new_q


