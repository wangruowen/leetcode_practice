# https://leetcode.com/problems/find-leaves-of-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        # DFS reach to leaf and then mark their parent's children to be None, and bottom up
        result = []
        def DFS(node, level=0):
            nonlocal result

            if not node.left and not node.right:
                # Is leaf
                if len(result) <= level:
                    result.append([])
                result[level].append(node.val)
                return None, level

            left_level = right_level = level
            if node.left:
                node.left, left_level = DFS(node.left, level)
            if node.right:
                node.right, right_level = DFS(node.right, level)

            if not node.left and not node.right:
                # After the children leaves are counted, now this node becomes a new leaf
                new_level = max(left_level, right_level) + 1
                if len(result) <= new_level:
                    result.append([])
                result[new_level].append(node.val)
                return None, new_level
            return node, level
        DFS(root)
        return result