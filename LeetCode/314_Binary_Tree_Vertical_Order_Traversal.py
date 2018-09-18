# https://www.geeksforgeeks.org/print-binary-tree-vertical-order/
from collections import defaultdict

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # BFS + hash dict
        position_dict = defaultdict(list)
        queue = [(root, 0)]
        while queue:
            node, i = queue.pop(0)
            position_dict[i].append(node.val)
            if node.left:
                queue.append((node.left, i - 1))
            if node.right:
                queue.append((node.right, i + 1))
        start, end = min(position_dict.keys()), max(position_dict.keys())
        result = []
        for j in range(start, end + 1):
            result.append(position_dict[j])
        return result

s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.left.right = TreeNode(8)
root.right.right = TreeNode(7)
root.right.right.right = TreeNode(9)
print(s.verticalOrder(root))