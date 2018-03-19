# https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys

class Solution(object):
    def __init__(self):
        self.min = 2**32

    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Take-away: In order can turn the BST tree to a sorted array
        inorder_array = []
        self.inorder(root, inorder_array)
        min = sys.maxint
        for i in range(len(inorder_array) - 1):
            if inorder_array[i + 1].val - inorder_array[i].val < min:
                min = inorder_array[i + 1].val - inorder_array[i].val
        return min

    def inorder(self, node, inorder_array):
        if node is None:
            return
        if node.left:
            self.inorder(node.left, inorder_array)
        inorder_array.append(node)
        if node.right:
            self.inorder(node.right, inorder_array)
