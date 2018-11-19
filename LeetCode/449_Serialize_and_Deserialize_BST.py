# https://leetcode.com/problems/serialize-and-deserialize-bst/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        # For BST tree,
        # in-order traversal and pre-order traversal work together
        preorder, inorder = [], []
        stack = [root]
        while len(stack) > 0:
            node = stack.pop()
            preorder.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return " ".join(map(str, preorder))

        # No need to do inorder, because inorder is for sure sorted. So we can just sort pre-order
        # stack = [root]
        # while len(stack) > 0:
        #     node = stack[-1]
        #     if node.left:
        #         stack.append(node.left)
        #         node.left = None
        #     else:
        #         node = stack.pop()
        #         inorder.append(node.val)
        #         if node.right:
        #             stack.append(node.right)
        # tmp = " ".join(map(str, preorder)) + "#" + " ".join(map(str, inorder))
        # # print(tmp)
        # return tmp


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None

        preorder = [int(x) for x in data.split()]
        inorder = sorted(preorder)

        # preorder, inorder = data.split("#")
        # preorder = [int(x) for x in preorder.split()]
        # inorder = [int(x) for x in inorder.split()]
        def buildTree(preor, inor):
            if len(preor) == 0:
                return None

            root = preor[0]
            root_index = inor.index(root)
            left_inor = inor[:root_index]
            right_inor = inor[root_index+1:]
            left_preor = preor[1:len(left_inor)+1]
            right_preor = preor[len(left_inor)+1:]
            root_node = TreeNode(root)
            root_node.left = buildTree(left_preor, left_inor)
            root_node.right = buildTree(right_preor, right_inor)
            return root_node
        return buildTree(preorder, inorder)


class Codec2:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        # Preorder Traversal
        if not root:
            return ""

        stack = [root]
        nodes = []
        while stack:
            node = stack.pop()
            nodes.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return ",".join(map(str, nodes))

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None
        from collections import deque
        q = deque(map(int, data.split(",")))
        def build(minval, maxval):
            if q and minval < q[0] < maxval:
                val = q.popleft()
                node = TreeNode(val)
                node.left = build(minval, val)
                node.right = build(val, maxval)
                return node
            return None

        return build(float('-inf'), float('inf'))


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))