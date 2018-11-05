# https://leetcode.com/problems/trim-a-binary-search-tree/description/
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        # DFS Pre-order traversal
        return self.helper(root, L, R)


    def helper(self, node, L, R):
        if node is None: return

        if node.val < L:
            # Only need look at the right subtree
            return self.helper(node.right, L, R)
        elif node.val > R:
            # Only need to look at the left subtree
            return self.helper(node.left, L, R)
        else:
            # within the range
            node.left = self.helper(node.left, L, R)
            node.right = self.helper(node.right, L, R)

        return node

    def trimBST_v2(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        # In order Iterative
        if not root:
            return None

        dummy_root = TreeNode(-1)
        dummy_root.left = root
        stack, parent_stack = [root], [[dummy_root, True]]
        while stack:
            cur = stack.pop()
            parent, is_left = parent_stack[-1]
            if cur.val < L:
                cur = cur.right
                if is_left:
                    parent.left = cur
                else:
                    parent.right = cur
                if cur:
                    stack.append(cur)
                else:
                    # the parent of cur has no is_left child anymore
                    parent_stack.pop()
            elif cur.val > R:
                cur = cur.left
                if is_left:
                    parent.left = cur
                else:
                    parent.right = cur
                if cur:
                    stack.append(cur)
                else:
                    parent_stack.pop()
            else:
                # Within the range
                # The parent to this cur node is fixed, no trim between this parent-child pair
                parent_stack.pop()
                # Preorder Iterative, first push right, then push left
                if cur.right:
                    stack.append(cur.right)
                    parent_stack.append([cur, False])
                if cur.left:
                    stack.append(cur.left)
                    parent_stack.append([cur, True])
        return dummy_root.left


s = Solution()
root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(2)






