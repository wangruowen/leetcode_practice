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
        if not root: return False
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