# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return

        cur_layer = [root]
        while cur_layer:
            new_layer = []
            last = None
            for node in cur_layer:
                if last:
                    last.next = node
                last = node
                if node.left:
                    new_layer.append(node.left)
                if node.right:
                    new_layer.append(node.right)
            cur_layer = new_layer
