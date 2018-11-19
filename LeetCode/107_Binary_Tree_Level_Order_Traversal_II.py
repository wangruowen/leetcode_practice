# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        from collections import deque
        q = deque()
        if not root:
            return []
        cur_layer = [root]
        while cur_layer:
            new_layer = []
            cur_layer_val = []
            for each in cur_layer:
                cur_layer_val.append(each.val)
                if each.left:
                    new_layer.append(each.left)
                if each.right:
                    new_layer.append(each.right)
            q.appendleft(cur_layer_val)
            cur_layer = new_layer
        return list(q)



