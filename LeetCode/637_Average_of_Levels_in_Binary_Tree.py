# https://leetcode.com/problems/average-of-levels-in-binary-tree/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        # BFS
        queue = [root]
        result = []
        while len(queue) > 0:
            new_queue = []
            level_vals = []
            while len(queue) > 0:
                node = queue.pop(0)
                level_vals.append(node.val)
                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)
            queue = new_queue
            result.append(float(sum(level_vals)) / len(level_vals))

        return result

