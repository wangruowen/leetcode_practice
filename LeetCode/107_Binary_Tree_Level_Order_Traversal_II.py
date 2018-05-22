# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/
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
        # BFS
        if not root:
            return []
        result = []
        queue = [root]

        while len(queue) > 0:
            result.insert(0, map(lambda x: x.val, queue))
            new_queue = []
            while len(queue) > 0:
                node = queue.pop(0)
                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)
            queue = new_queue
        return result
