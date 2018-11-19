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

    def deleteNode_v2(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return None
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # key == root.val
            # If root is leaf, then just delete it
            if not root.left and not root.right:
                root = None
            elif not root.left:
                root = root.right
            elif not root.right:
                root = root.left
            else:
                # Both left and right exist
                # use the most left child on the right side to replace
                last, node = None, root.right
                while node.left:
                    last, node = node, node.left
                root.val = node.val
                if last:
                    last.left = node.right
                else:
                    root.right = node.right

        return root

    def deleteNode_v3(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return None
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # key == root.val
            # We use root.right to replace root
            # the original root.right.left will be put
            # on the most right child of the root.left
            if root.right:
                new_root = root.right
                if root.left:
                    tmp = root.left
                    while tmp.right:
                        tmp = tmp.right
                    tmp.right = root.right.left
                    new_root.left = root.left
                root = new_root
            elif root.left:
                root = root.left
            else:
                root = None

        return root