__author__ = 'Ruowen'
# https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        cur_layer = [root]
        while len(cur_layer) > 0:
            new_layer = []
            for each_node in cur_layer:
                if each_node:
                    new_layer.append(each_node.left)
                    new_layer.append(each_node.right)
            # Now check new_layer is symmetric
            length = len(new_layer)
            for i in range(0, length / 2):
                if (not new_layer[i] and not new_layer[length - 1 - i]) \
                    or (new_layer[i] and new_layer[length - 1 - i] \
                    and new_layer[i].val == new_layer[length - 1 - i].val):
                    pass
                else:
                    return False
            cur_layer = new_layer
        return True

    def isSymmetric_iterative(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack = []  # Keep every pair for checking
        if not root: return True
        stack.append([root.left, root.right])
        while stack:
            left, right = stack.pop()
            if not left and not right:
                continue

            if not left or not right or left.val != right.val:
                return False

            stack.append([left.left, right.right])
            stack.append([left.right, right.left])

        return True

    def isSymmetric_Recursive(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(leftnode, rightnode):
            if not leftnode and not rightnode:
                return True
            if not leftnode or not rightnode or leftnode.val != rightnode.val:
                return False

            return helper(leftnode.left, rightnode.right) and helper(leftnode.right, rightnode.left)

        if not root: return True
        return helper(root.left, root.right)