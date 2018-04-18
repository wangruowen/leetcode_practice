# https://leetcode.com/problems/sudoku-solver/description/
# import importlib
# valid_sudoku = importlib.import_module("36_Valid_Sudoku").Solution()

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board) != 9 or len(board[0]) != 9:
            return
        self.helper(board, 0, 0)

    def helper(self, board, i, j):
        if board[i][j] == ".":
            exist_bitmap = 0
            # Check row
            for s_j in range(9):
                if board[i][s_j] != ".":
                    exist_bitmap |= (1 << int(board[i][s_j]))
            # Check col
            for s_i in range(9):
                if board[s_i][j] != ".":
                    exist_bitmap |= (1 << int(board[s_i][j]))
            # Check block
            b = i / 3 * 3 + j / 3
            for b_i in range(b / 3 * 3, (b / 3 + 1) * 3):
                for b_j in range(b % 3 * 3, (b % 3 + 1) * 3):
                    if board[b_i][b_j] != ".":
                        exist_bitmap |= (1 << int(board[b_i][b_j]))

            for each_try in range(1, 10):
                if exist_bitmap & (1 << each_try) != 0:
                    continue
                board[i][j] = str(each_try)
                if i == 8 and j == 8:
                    # Done!
                    return True
                else:
                    if j < 8:
                        new_i, new_j = i, j + 1
                    else:
                        new_i, new_j = i + 1, 0
                    if self.helper(board, new_i, new_j):
                        return True
                    else:
                        board[i][j] = "."
                    # else, we continue the for loop

            # If all values are tried and none works
            # Rollback the current value, so that the parent and parent callers can try something different
            # board[i][j] = "."
            return False

        elif i == 8 and j == 8:
            # reach to the last node:
            return True
        else:
            if j < 8:
                i, j = i, j + 1
            else:
                i, j = i + 1, 0
            return self.helper(board, i, j)

import pprint
s = Solution()
board = \
[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

pprint.pprint(board)
s.solveSudoku(board)
pprint.pprint(board)