# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/
# Definition for a binary tree node.
from collections import deque

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        # BFS to achieve LeetCode standard tree representation
        result = []
        queue = deque([root])
        while len(queue) > 0:
            node = queue.popleft()
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("")

        return ",".join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        nodes = data.split(",")
        root = TreeNode(int(nodes[0])) if nodes[0] != '' else None
        if not root: return root
        cur_layer, next_layer = deque([root]), deque([])
        i, cur_parent_left_done = 1, False
        while i < len(nodes):
            cur_node = TreeNode(int(nodes[i])) if nodes[i] != '' else None
            cur_parent = cur_layer[0]
            if not cur_parent_left_done:
                cur_parent.left = cur_node
                cur_parent_left_done = True
            else:
                cur_parent.right = cur_node
                cur_layer.popleft()
                cur_parent_left_done = False
            if cur_node:
                next_layer.append(cur_node)
            if len(cur_layer) == 0:
                cur_layer, next_layer = next_layer, deque([])
            i += 1
        return root




# Your Codec object will be instantiated and called as such:
root = TreeNode(1)
root.left, root.right = TreeNode(2), TreeNode(3)
root.right.left, root.right.right = TreeNode(4), TreeNode(5)

codec = Codec()
print(codec.serialize(root))
codec.deserialize(codec.serialize(root))