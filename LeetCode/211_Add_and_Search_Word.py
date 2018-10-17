# https://leetcode.com/problems/add-and-search-word-data-structure-design/description/
class TrieNode:
    def __init__(self, letter):
        self.letter = letter
        self.children = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode(-1)

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode(c)
            node = node.children[c]
        node.is_word = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        def helper(rest_word, cand_nodes):
            if len(rest_word) > 0 and len(cand_nodes) == 0:
                return False
            if len(rest_word) == 0:
                for each in cand_nodes:
                    if each.is_word:
                        return True
                return False

            if rest_word[0] == '.':
                new_cand_nodes = [v for node in cand_nodes for k, v in node.children.items()]
            else:
                new_cand_nodes = [node.children[rest_word[0]] for node in cand_nodes if rest_word[0] in node.children]
            return helper(rest_word[1:], new_cand_nodes)

        return helper(word, [self.root])



# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord("bad")
obj.addWord("dad")
obj.addWord("mad")
print(obj.search("pad"))
print(obj.search("bad"))
print(obj.search(".ad"))
print(obj.search("b.."))
