# https://leetcode.com/problems/find-largest-value-in-each-tree-row/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # BFS
        result = []
        queue = [root] if root else []
        while len(queue) > 0:
            result.append(max(map(lambda x:x.val, queue)))
            new_queue = []
            for each in queue:
                if each.left:
                    new_queue.append(each.left)
                if each.right:
                    new_queue.append(each.right)
            queue = new_queue
        return result