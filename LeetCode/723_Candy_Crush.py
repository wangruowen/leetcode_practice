# http://www.cnblogs.com/grandyang/p/7858414.html
class Solution(object):
    def candyCrush(self, board):
        """
        :type board: List[List[int]]
        :rtype: List[List[int]]
        """
        row_len, col_len = len(board), len(board[0])

        while True:
            changed = False
            for i in range(row_len):
                for j in range(col_len):
                    if board[i][j] == 0:
                        continue
                    val = abs(board[i][j])
                    # Vertical
                    di = 1
                    while i + di < row_len and abs(board[i + di][j]) == val:
                        di += 1
                    # Mark them to be negative, which will be cleared as 0
                    if di > 2:
                        changed = True
                        for ddi in range(di):
                            board[i + ddi][j] = -abs(val)
                    # Horizontal
                    dj = 1
                    while j + dj < col_len and abs(board[i][j + dj]) == val:
                        dj += 1
                    if dj > 2:
                        changed = True
                        for ddj in range(dj):
                            board[i][j + ddj] = -abs(val)

            if not changed:
                break

            # Move negative to the top and then mark them as 0
            for j in range(col_len):
                k = i = row_len - 1
                while k >= 0:
                    if board[k][j] > 0:
                        board[i][j] = board[k][j]
                        print("board[%d][%d] = %d" % (i, j, board[i][j]))
                        i -= 1
                    k -= 1
                # Set 0 to 0-th to i-th item
                for k in range(i + 1):
                    board[k][j] = 0

        return board

s = Solution()
board = [[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]]
expected = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[110,0,0,0,114],[210,0,0,0,214],[310,0,0,113,314],[410,0,0,213,414],[610,211,112,313,614],[710,311,412,613,714],[810,411,512,713,1014]]
s.candyCrush(board)
print(board == expected)
