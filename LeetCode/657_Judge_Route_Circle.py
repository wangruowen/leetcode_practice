# https://leetcode.com/problems/judge-route-circle/description/
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x, y = 0, 0
        for each_move in moves:
            if each_move == 'R':
                x -= 1
            elif each_move == 'L':
                x += 1
            elif each_move == 'U':
                y += 1
            elif each_move == 'D':
                y -= 1

        if x == 0 and y == 0:
            return True
        else:
            return False
        """
        return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')
        """