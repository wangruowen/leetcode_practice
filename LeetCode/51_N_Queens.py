# https://leetcode.com/problems/n-queens/
class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        result = []
        one_set = [['.' for _ in range(n)] for _ in range(n)]

        def can_place_Q(i, j, exist_queens_pos):
            for ei, ej in exist_queens_pos:
                if ei == i or ej == j or abs(ei - i) == abs(ej - j):
                    return False
            return True

        def helper(i, cur_set, exist_queens_pos=[]):
            if i == n:
                one_result = []
                for each_row in cur_set:
                    one_result.append("".join(each_row))
                result.append(one_result)
                return

            # For each row i, we put one queen
            for j in range(n):
                if can_place_Q(i, j, exist_queens_pos):
                    cur_set[i][j] = 'Q'
                    exist_queens_pos.append((i, j))
                    helper(i + 1, cur_set)
                    exist_queens_pos.pop()
                    cur_set[i][j] = '.'

        helper(0, one_set)
        return result
