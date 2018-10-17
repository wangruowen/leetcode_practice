# https://leetcode.com/problems/find-duplicate-subtrees/description/
from hashlib import sha1

class Solution:
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        # Post-Order Traversal to build Merkle Hash Tree
        if not root: return []
        def helper(node):
            left_hash = helper(node.left) if node.left else "#"
            right_hash = helper(node.right) if node.right else "#"
            node.hash_val = sha1((left_hash + str(node.val) + right_hash).encode("utf-8")).hexdigest()
            return node.hash_val
        helper(root)

        dup_nodes = []
        visited, dup_val = set(), set()
        def find_match(node):
            if node.hash_val in visited and node.hash_val not in dup_val:
                dup_nodes.append(node)
                dup_val.add(node.hash_val)
            visited.add(node.hash_val)
            if node.left:
                find_match(node.left)
            if node.right:
                find_match(node.right)
        find_match(root)

        return dup_nodes