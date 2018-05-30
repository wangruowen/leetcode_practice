# https://leetcode.com/problems/map-sum-pairs/description/
class TrieNode(object):
    def __init__(self, parent):
        self.parent = parent
        self.children = {}
        self.val = 0
        self.is_key = False

class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie_root = TrieNode(None)

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        cur_node = self.trie_root
        for each_letter in key:
            if each_letter in cur_node.children:
                cur_node = cur_node.children[each_letter]
            else:
                tmp_node = TrieNode(cur_node)
                cur_node.children[each_letter] = tmp_node
                cur_node = tmp_node
        if cur_node.is_key:
            # Then this node already exists, so we override value to the leaf node
            diff = val - cur_node.val
            cur_node.val = val
        else:
            # This could be a newly created TrieNode, or a path node
            # either way, we transform it to a key node
            cur_node.is_key = True
            diff = val
            cur_node.val += val

        # Now back-propagate to the root to update val
        cur_node = cur_node.parent
        while cur_node:
            cur_node.val += diff
            cur_node = cur_node.parent

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        cur_node = self.trie_root
        for each_letter in prefix:
            if each_letter in cur_node.children:
                cur_node = cur_node.children[each_letter]
            else:
                return 0
        return cur_node.val


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)