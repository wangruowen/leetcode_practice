# https://leetcode.com/problems/longest-word-in-dictionary/description/
class TreeNode:
    def __init__(self, val):
        self.children = {}
        self.val = val
        self.word = None


class Solution:
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        root = TreeNode(-1)
        # Build Tri
        for each in sorted(words):
            node = root
            for c in each:
                if c in node.children:
                    node = node.children[c]
                else:
                    new_node = TreeNode(c)
                    node.children[c] = new_node
                    node = new_node
            node.word = each  # Notify this word exists

        longest_word = ""
        queue = [root]
        while len(queue) > 0:
            cur = queue.pop(0)
            for each_node in cur.children.values():
                if each_node.word:
                    if len(each_node.word) > len(longest_word) or each_node.word < longest_word:
                        longest_word = each_node.word
                    queue.append(each_node)  # Only enqueue exist words

        return longest_word

s = Solution()
# words = ["w","wo","wor","worl","world"]
words = ["rac","rs","ra","on","r","otif","o","onpdu","rsf","rs","ot","oti","racy","onpd"]
print(s.longestWord(words))