# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # Get root from preorder, 
        # Get left child from inorder[:root_idx]
        # Get right child from inorder[root_idx+1:]
        if len(preorder) == 0:
            return None

        root = preorder[0]
        root_idx = inorder.index(root)
        left_inorder, right_inorder = inorder[:root_idx], inorder[root_idx + 1:]
        left_preorder = preorder[1:1+len(left_inorder)]
        right_preorder = preorder[1+len(left_inorder):]
        node = TreeNode(root)
        node.left = self.buildTree(left_preorder, left_inorder)
        node.right = self.buildTree(right_preorder, right_inorder)

        return node
