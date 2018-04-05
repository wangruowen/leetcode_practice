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

s = Solution()
board = \
[["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
word = "ABCESEEEFS"

print(s.exist(board, word))