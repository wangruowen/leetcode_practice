# https://leetcode.com/problems/game-of-life/

class Solution(object):
    def getOriValue(self, board, i, j):
        if i < 0  or j < 0 or i >= self.row_num or j >= self.col_num:
            return None

        if self.change_status[i][j]:
            ori_value = 1 - board[i][j]
        else:
            ori_value = board[i][j]

        return ori_value

    def computeNextState(self, board, i, j):
        current_value = self.getOriValue(board, i, j)
        count_lives = 0
        for sur_x, sur_y in ((-1, -1), (-1, 0), (-1, 1),
                             ( 0, -1),          ( 0, 1),
                             ( 1, -1), ( 1, 0), ( 1, 1)):
            surround_value = self.getOriValue(board, i + sur_x, j + sur_y)
            if surround_value is not None and surround_value == 1:
                count_lives += 1

        new_value, is_changed = current_value, False
        if current_value == 1:
            if count_lives < 2:
                new_value, is_changed = 0, True
            if count_lives > 3:
                new_value, is_changed = 0, True
        else:
            if count_lives == 3:
                new_value, is_changed = 1, True

        return new_value, is_changed

    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.row_num = len(board)
        self.col_num = len(board[0])
        # ATTENTION! In Python, initialize 2D list should be careful
        self.change_status = [[False for i in range(self.col_num)] for j in range(self.row_num)]

        for i in range(self.row_num):
            for j in range(self.col_num):
                new_value, is_changed = self.computeNextState(board, i, j)
                board[i][j] = new_value
                self.change_status[i][j] = is_changed


# test
board = [[0, 1, 1],
         [1, 0, 1],
         [1, 0, 1]]

s = Solution()
s.gameOfLife(board)
print(board)