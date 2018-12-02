# https://leetcode.com/problems/word-search/description/
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # DFS
        # Find the starting char
        self.word = word
        self.row_len = len(board)
        self.col_len = len(board[0])
        for i in range(self.row_len):
            for j in range(self.col_len):
                if word[0] == board[i][j]:
                    # Now let's start
                    if self.DFS(board, i, j, 0):
                        return True

        return False

    def DFS(self, board, i, j, word_index):
        cur_char = self.word[word_index]
        if board[i][j] == cur_char:
            board[i][j] = '0'  # Temporarily mark

            if word_index == len(self.word) - 1:
                return True
            next_char = self.word[word_index + 1]
            if i > 0 and board[i - 1][j] == next_char and \
                    self.DFS(board, i - 1, j, word_index + 1):
                return True
            if i < self.row_len - 1 and board[i + 1][j] == next_char and \
                    self.DFS(board, i + 1, j, word_index + 1):
                return True
            if j > 0 and board[i][j - 1] == next_char and \
                    self.DFS(board, i, j - 1, word_index + 1):
                return True
            if j < self.col_len - 1 and board[i][j + 1] == next_char and \
                    self.DFS(board, i, j + 1, word_index + 1):
                return True

            board[i][j] = cur_char  # Rollback if all explores fail
        return False

    def copy(self, board):
        return [row[:] for row in board]

    def exist_v2(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        rowlen, collen = len(board), len(board[0])

        def DFS(i, j, word_index):
            if board[i][j] == word[word_index]:
                word_index += 1
                if word_index == len(word):
                    return True

                for di, dj in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                    ip, jp = i + di, j + dj
                    if 0 <= ip < rowlen and 0 <= jp < collen and (ip, jp) not in visited:
                        visited.add((ip, jp))
                        if DFS(ip, jp, word_index):
                            return True
                        visited.remove((ip, jp))
            return False

        for i in range(rowlen):
            for j in range(collen):
                visited = set([(i, j)])
                if DFS(i, j, 0):
                    return True
        return False

s = Solution()
board = \
[["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
word = "ABCESEEEFS"

print(s.exist(board, word))