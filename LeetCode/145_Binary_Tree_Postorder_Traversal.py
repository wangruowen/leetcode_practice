# https://leetcode.com/problems/binary-tree-postorder-traversal/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        stack, result = [], []
        cur = root
        while cur:
            if not cur.left and not cur.right:
                result.append(cur.val)
                if stack:
                    cur = stack.pop()
                    continue
                else:
                    break

            while cur.left:
                stack.append(cur)
                cur = cur.left
                stack[-1].left = None
            if cur.right:
                stack.append(cur)
                cur = cur.right
                stack[-1].right = None

        return result

    def postorderTraversal_v2(self, root):
        if not root:
            return []
        stack, result = [None], []
        visited = set()
        node = root
        while node:
            while node.left and node.left not in visited:
                stack.append(node)
                node = node.left
            if node.right and node.right not in visited:
                stack.append(node)
                node = node.right
            else:
                result.append(node.val)
                visited.add(node)
                node = stack.pop()
        return result
