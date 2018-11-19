"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """
        node_list = []

        def helper(node, node_list):
            if not node:
                return
            node_list.append(node.val)
            node_list.append(len(node.children))
            for each in node.children:
                helper(each, node_list)

        helper(root, node_list)
        return " ".join(map(str, node_list))

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """
        if data == "":
            return None
        q = data.split(" ")

        def helper(q):
            if len(q) == 0:
                return None
            root = Node(int(q.pop(0)), [])
            children_size = int(q.pop(0))
            for _ in range(children_size):
                root.children.append(helper(q))
            return root

        return helper(q)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

class Codec_v2:
    def serialize(self, root):
        """
        Encode a N-ary tree to a string
        :param root:
        :return:
        """
        # Like JSON, a Tree like following
        #         1
        #      2  3  4
        #     5 6    7 8 9
        # Could be 1[2[5[]6[]]3[]4[7[]8[]9[]]]
        if not root:
            return ""

        children = []
        for each_child in root.children:
            children.append(self.serialize(each_child))
        return "{}[{}]".format(root.val, "".join(children))

    def deserialize(self, data):
        """
        Decode a string to reconstruct a N-ary tree
        :param data:
        :return:
        """
        if data == "":
            return None

        # Given a string: 1[2[5[]6[]]3[]4[7[]8[]9[]]]
        open_bracket = data.find("[")
        root = Node(int(data[:open_bracket]), [])
        children_data = data[open_bracket + 1:-1]
        # 2[5[]6[]]3[]4[7[]8[]9[]]
        if children_data == "":
            return root

        def get_children(children_data):
            children = []
            open_bracket = children_data.find("[")
            while open_bracket >= 0:
                cur_child = Node(int(children_data[:open_bracket]), [])
                # print(cur_child.val, children_data[first_colon+1:])
                stack = []
                i = open_bracket
                # print(children_data[i:])
                while i < len(children_data):
                    if children_data[i] == '[':
                        stack.append('[')
                    elif children_data[i] == ']':
                        stack.pop()
                    if len(stack) == 0:
                        break
                    i += 1
                # print("children: ", children_data[first_colon + 2:i-1])
                cur_child.children = get_children(children_data[open_bracket + 1:i])
                # print(children_data[first_colon + 2:i])
                children.append(cur_child)
                children_data = children_data[i + 1:]
                open_bracket = children_data.find("[")

            return children

        root.children = get_children(children_data)
        return root