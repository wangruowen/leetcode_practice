# https://leetcode.com/problems/recover-binary-search-tree/description/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def inorder(self, node):
        if not node:
            return
        self.inorder(node.left)

        if self.left_node.val >= node.val:
            if not self.first_wrong:
                self.first_wrong = self.left_node
            # Keep update the second_wrong
            self.second_wrong = node
        self.left_node = node

        self.inorder(node.right)

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        # Inorder Traversal
        # For a valid BST, the left node < node
        self.first_wrong, self.second_wrong = None, None
        self.left_node = TreeNode(float('-inf'))

        self.inorder(root)
        self.first_wrong.val, self.second_wrong.val = self.second_wrong.val, self.first_wrong.val


s = Solution()
root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(2)
# root.right.left = TreeNode(2)
s.recoverTree(root)