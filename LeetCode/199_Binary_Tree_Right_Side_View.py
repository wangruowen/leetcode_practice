# https://leetcode.com/problems/binary-tree-right-side-view/description/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # BFS
        if not root:
            return []
        queue = [root, "#"]
        result = []
        last = None
        while len(queue) > 0:
            node = queue.pop(0)
            if node == "#":
                # end of line
                if last and last != "#":
                    result.append(last.val)
                    queue.append(node)
            else:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            last = node
        return result

s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
root.right.right = TreeNode(4)
print(s.rightSideView(root))