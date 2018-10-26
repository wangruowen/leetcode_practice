# https://leetcode.com/problems/word-break/
class TrieNode:
    def __init__(self, val=None):
        self.val = val
        self.children = {}
        self.word = None

class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # Trie + Backtracking
        def buildTrie(wordDict):
            root = TrieNode()
            for word in wordDict:
                node = root
                for c in word:
                    if c not in node.children:
                        node.children[c] = TrieNode(c)
                    node = node.children[c]
                node.word = word
            return root
        root = buildTrie(wordDict)

        def helper(s):
            if s == "":
                return True
            i = 0
            node = root
            while i < len(s):
                if s[i] not in node.children:
                    return False
                elif node.children[s[i]].word and helper(s[i+1:]):
                    return True
                    # If the recursive call doesn't return True,
                    # then we try to find the next matched word
                else:
                    node = node.children[s[i]]
                i += 1
            return False
        return helper(s)

s = Solution()
test_s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
print(s.wordBreak(test_s, wordDict))





