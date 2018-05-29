# https://leetcode.com/problems/battleships-in-a-board/description/
class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        count = 0
        row_len, col_len = len(board), len(board[0])
        i, j = 0, 0
        while i < row_len and j < col_len:
            if board[i][j] == 'X' and self.is_start_point(board, i, j):
                count += 1
            j += 1
            if j == col_len:
                j = 0
                i += 1

        return count

    def is_start_point(self, board, i, j):
        if (i > 0 and board[i - 1][j] == 'X') or (j > 0 and board[i][j - 1] == 'X'):
            return False
        else:
            return True

    # def DFS(self, board, i, j):
    #     if (i > 0 and board[i - 1][j] == 'X') or (j > 0 and board[i][j - 1] == 'X'):
    #         # We already visisted, because this i, j is not the starting point
    #
    #
    #     is_horizontal = False
    #     while j < self.col_len - 1 and board[i][j + 1] == 'X':
    #         is_horizontal = True
    #         j += 1
    #     if not is_horizontal:
    #         while i < self.row_len - 1 and board[i + 1][j] == 'X':
    #             i += 1
    #     self.count += 1
    #     return i, j

s = Solution()
board = ["X..X", "...X", "...X"]
print(s.countBattleships(board))