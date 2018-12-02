# https://leetcode.com/problems/word-search-ii/
class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        def buildTrie():
            root = TrieNode("")
            for word in words:
                cur = root
                for c in word:
                    if c not in cur.children:
                        node = TrieNode(c)
                        cur.children[c] = node
                    cur = cur.children[c]
                cur.word = word
            return root

        def DFS(i, j, node, visited):
            """
            We call this DFS if board[i][j] is already matched with node.val and we want to
            recursively check whether its 4-directional cells could match the node.children
            :param i:
            :param j:
            :param node:
            :param visited:
            :return:
            """
            nonlocal result, row_len, col_len

            if node.word:
                result.add(node.word)

            for di, dj in [[-1,0],[1,0],[0,1],[0,-1]]:
                new_i, new_j = i+di, j+dj
                if 0 <= new_i < row_len and 0 <= new_j < col_len and \
                        board[new_i][new_j] in node.children and (new_i, new_j) not in visited:
                    visited.append((new_i, new_j))
                    DFS(new_i, new_j, node.children[board[new_i][new_j]], visited)
                    visited.pop()

        root = buildTrie()
        result = set()
        row_len, col_len = len(board), len(board[0])
        for i in range(row_len):
            for j in range(col_len):
                if board[i][j] in root.children:
                    visited = [(i, j)]
                    find_words = DFS(i, j, root.children[board[i][j]], visited)
                    if find_words:
                        result.extend(find_words)
        return list(result)