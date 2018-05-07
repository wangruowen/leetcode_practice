# https://leetcode.com/problems/delete-node-in-a-bst/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # root is the key
            if root.left:
                # We promote the root.left to be the new root
                # root.left.right will be attached to the most left
                # of root.right if root.right exists
                new_root = root.left
                if root.right:
                    if new_root.right:
                        tmp = root.right
                        while tmp.left:
                            tmp = tmp.left
                        tmp.left = new_root.right
                        new_root.right = root.right
                    else:
                        new_root.right = root.right
            elif root.right:
                # We promote the root.right to be the new root
                new_root = root.right
            else:
                # root is leaf
                new_root = None
            root = new_root

        return root

