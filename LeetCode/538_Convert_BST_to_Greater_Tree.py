# https://leetcode.com/problems/convert-bst-to-greater-tree/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        stack = []
        self.prepare_stack(root, stack)
        # Now let's pop the stack
        accumulated_value = 0
        while len(stack) > 0:
            cur_node = stack.pop()
            cur_node.val += accumulated_value
            accumulated_value = cur_node.val

        return root

    def prepare_stack(self, node, stack):
        """
        Prepare the stack by inorder-pushing left tree, cur node and right tree into it
        :param node:
        :param stack:
        :return:
        """
        if node is None:
            return

        if node.left is not None:
            self.prepare_stack(node.left, stack)
        stack.append(node)
        if node.right is not None:
            self.prepare_stack(node.right, stack)


