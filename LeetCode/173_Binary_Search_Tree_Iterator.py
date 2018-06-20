# https://leetcode.com/problems/binary-search-tree-iterator/description/
# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        cur_node = root
        while cur_node:
            self.stack.append(cur_node)
            cur_node = cur_node.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) > 0

    def next(self):
        """
        :rtype: int
        """
        top = None
        if len(self.stack) > 0:
            top = self.stack.pop()
            cur_node = top.right
            while cur_node:
                self.stack.append(cur_node)
                cur_node = cur_node.left

        return top.val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())