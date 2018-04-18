__author__ = 'ruowen.wang'
# https://leetcode.com/problems/valid-sudoku/

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if len(board) != 9 or len(board[0]) != 9:
            return False

        # Every row
        for i in range(9):
            bitmap = 0
            for j in range(9):
                if board[i][j] == '.':
                    continue
                val = 1 << int(board[i][j])
                if bitmap & val != 0:
                    return False
                else:
                    bitmap |= val

        # Every column
        for j in range(9):
            bitmap = 0
            for i in range(9):
                if board[i][j] == '.':
                    continue
                val = 1 << int(board[i][j])
                if bitmap & val != 0:
                    return False
                else:
                    bitmap |= val

        # Every block
        for b in range(9):
            bitmap = 0
            # b = 0/1/2, i = 0/1/2, b = 3/4/5, i = 3/4/5, b = 6/7/8, i = 6/7/8
            # b = 0/3/6, j = 0/1/2, b = 1/4/7, j = 3/4/5, b = 2/5/8, j = 6/7/8
            for i in range(b / 3 * 3, (b / 3 + 1) * 3):
                for j in range(b % 3 * 3, (b % 3 + 1) * 3):
                    if board[i][j] == '.':
                        continue
                    val = 1 << int(board[i][j])
                    if bitmap & val != 0:
                        return False
                    else:
                        bitmap |= val

        return True

