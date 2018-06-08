# https://leetcode.com/problems/add-one-row-to-tree/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if not root:
            if d == 1:
                return TreeNode(v)
            return root
        if d == 1:
            new_root = TreeNode(v)
            new_root.left = root
            return new_root

        # BFS to find d - 1 level first
        queue = [root]
        cur_d = 1
        while len(queue) > 0:
            if cur_d == d - 1:
                break
            new_queue = []
            while len(queue) > 0:
                node = queue.pop(0)
                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)
            queue = new_queue
            cur_d += 1

        for node in queue:
            old_left, old_right = node.left, node.right
            new_left, new_right = TreeNode(v), TreeNode(v)
            node.left, node.right = new_left, new_right
            new_left.left, new_right.right = old_left, old_right

        return root