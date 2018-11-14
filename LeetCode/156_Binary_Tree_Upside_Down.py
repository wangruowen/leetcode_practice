# https://blog.csdn.net/whuwangyi/article/details/43186045
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # @param root, a tree node
    # @return root of the upside down tree
    def upsideDownBinaryTree(self, root):
        # Imagine
        #    1        2
        #   / \      / \
        #  2  3  =>  3  1
        parent, cur, prev_right = None, root, None
        while cur:
            left = cur.left
            cur.left = prev_right
            prev_right = cur.right
            cur.right = parent
            parent, cur = cur, left
        return parent


