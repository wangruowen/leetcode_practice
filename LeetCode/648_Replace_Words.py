# https://leetcode.com/problems/replace-words/description/
class TrieNode(object):
    def __init__(self, val):
        self.children = {}
        self.val = val
        self.word = None

class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        # Trie/Prefix Tree
        result = []
        root = self.buildTrie(dict)
        for each in sentence.split():
            prefix = self.searchTrie(root, each)
            if prefix:
                result.append(prefix)
            else:
                result.append(each)
        return " ".join(result)

    def buildTrie(self, dict):
        root = TrieNode(-1)
        for each in dict:
            node = root
            for c in each:
                if c in node.children:
                    node = node.children[c]
                else:
                    new_node = TrieNode(c)
                    node.children[c] = new_node
                    node = new_node
            node.word = each
        return root

    def searchTrie(self, node, word):
        for c in word:
            if c in node.children:
                node = node.children[c]
                if node.word:
                    break
            else:
                break
        return node.word

s = Solution()
dict = ["a", "aa", "aaa", "aaaa"]
sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
print(s.replaceWords(dict, sentence))