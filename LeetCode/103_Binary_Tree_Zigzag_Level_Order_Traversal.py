# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from queue import deque

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # BFS layer-by-layer
        result = []
        if not root:
            return result
        q = deque([root])

        forward = True
        while q:
            new_q = deque()
            cur_layer = []
            while q:
                node = q.popleft()
                cur_layer.append(node.val)
                if node.left:
                    new_q.append(node.left)
                if node.right:
                    new_q.append(node.right)
            q = new_q
            if forward:
                result.append(cur_layer)
            else:
                result.append(cur_layer[::-1])
            forward = not forward
        return result

    def zigzagLevelOrder_v2(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # Do the same layer-by-layer BFS as usual,
        # use a forward flag to reverse the values if needed
        if not root:
            return []

        result = []
        cur_layer = [root]
        forward = True
        while cur_layer:
            cur_vals, new_layer = [], []
            for each in cur_layer:
                cur_vals.append(each.val)
                if each.left:
                    new_layer.append(each.left)
                if each.right:
                    new_layer.append(each.right)
            if not forward:
                result.append(cur_vals[::-1])
            else:
                result.append(cur_vals)
            forward = not forward
            cur_layer = new_layer
        return result

s = Solution()
root = TreeNode(1)
