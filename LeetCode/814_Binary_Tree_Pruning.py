# https://leetcode.com/problems/binary-tree-pruning/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # DFS Postorder Traversal
        return self.helper(root)

    def helper(self, node):
        if not node:
            return None

        if node.left:
            node.left = self.helper(node.left)
        if node.right:
            node.right = self.helper(node.right)
        if not node.left and not node.right and node.val == 0:
            # Remove this node
            return None
        return node
