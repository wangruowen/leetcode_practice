# https://leetcode.com/problems/subtree-of-another-tree/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from hashlib import sha256

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        # Merkle Hash Tree
        # DFS build hash value by Post-order Traversal
        # Another way could be turn into Inorder string and do string comparison
        def hash(x):
            sha = sha256()
            sha.update(x)
            return sha.hexdigest()

        def buildMHT(root):
            if not root:
                return ""
            left_hash = buildMHT(root.left)
            right_hash = buildMHT(root.right)
            root.val = hash(str(root.val) + left_hash + right_hash)
            return root.val

        buildMHT(s)
        buildMHT(t)

        queue = [s]
        while len(queue) > 0:
            node = queue.pop(0)
            if node.val == t.val:
                return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False



