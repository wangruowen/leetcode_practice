# https://leetcode.com/problems/minesweeper/description/
class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        # DFS
        i, j = click[0], click[1]
        if board[i][j] == 'M':
            board[i][j] = 'X'
            return board
        elif board[i][j] == 'E':
            self.reveal_more(board, i, j)

        return board

    def reveal_more(self, board, i, j):
        num_adj_mines = 0
        for di, dj in [(-1, 0), (1, 0), (0, 1), (0, -1), (-1, -1), (1, 1), (-1, 1), (1, -1)]:
            if i + di >= 0 and i + di < len(board) and j + dj >= 0 and j + dj < len(board[0]):
                if board[i + di][j + dj] == 'M':
                    num_adj_mines += 1
        if num_adj_mines > 0:
            board[i][j] = str(num_adj_mines)
        else:
            board[i][j] = 'B'
            for di, dj in [(-1, 0), (1, 0), (0, 1), (0, -1), (-1, -1), (1, 1), (-1, 1), (1, -1)]:
                if i + di >= 0 and i + di < len(board) and j + dj >= 0 and j + dj < len(board[0]):
                    if board[i + di][j + dj] == 'E':
                        self.reveal_more(board, i + di, j + dj)

s = Solution()
board = \
[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]
click = [1, 2]
print(s.updateBoard(board, click))





