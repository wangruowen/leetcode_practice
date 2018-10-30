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

s = Solution()
root = TreeNode(1)
