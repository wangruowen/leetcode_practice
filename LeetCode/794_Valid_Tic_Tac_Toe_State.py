# https://leetcode.com/problems/valid-tic-tac-toe-state/description/
class Solution:
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        if len(board) != 3:
            return False

        X_num, O_num, E_num = 0, 0, 0
        X_win, O_win = False, False
        for row in board:
            if len(row) != 3:
                return False

            if row == "XXX":
                X_win = True
            elif row == "OOO":
                O_win = True

            for i in row:
                if i == 'X':
                    X_num += 1
                elif i == 'O':
                    O_num += 1
                elif i == ' ':
                    E_num += 1
        # X_num at most is 1 more than O_num
        if X_num - 1 == O_num or X_num == O_num:
            pass
        else:
            return False

        for j in range(3):
            if board[0][j] == 'X' and board[1][j] == board[2][j] == 'X':
                X_win = True
            elif board[0][j] == 'O' and board[1][j] == board[2][j] == 'O':
                O_win = True
        if board[1][1] == 'X' and (board[0][0] == board[2][2] == 'X' or
                board[0][2] == board[2][0] == 'X'):
            X_win = True
        if board[1][1] == 'O' and (board[0][0] == board[2][2] == 'O' or
                board[0][2] == board[2][0] == 'O'):
            O_win = True

        if X_win and O_win:
            return False
        if X_win:
            return X_num - 1 == O_num
        elif O_win:
            return O_num == X_num

        return True

