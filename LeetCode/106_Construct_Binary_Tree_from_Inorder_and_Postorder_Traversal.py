# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        # Get root from the last item in postorder
        # Get left subtree from inorder[:root]
        # Get right subtree from inorder[root+1:]
        if len(inorder) == 0:
            return None
        root_idx = inorder.index(postorder[-1])
        left_inorder = inorder[:root_idx]
        right_inorder = inorder[root_idx+1:]
        left_postorder = postorder[:len(left_inorder)]
        right_postorder = postorder[len(left_inorder):-1]
        node = TreeNode(postorder[-1])
        node.left = self.buildTree(left_inorder, left_postorder)
        node.right = self.buildTree(right_inorder, right_postorder)
        return node