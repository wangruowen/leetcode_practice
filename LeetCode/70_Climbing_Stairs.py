__author__ = 'Ruowen'

# https://leetcode.com/problems/climbing-stairs/
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        steps = [1, 2]
        for i in range(3, n + 1):
            steps.insert(i - 1, steps[i - 3] + steps[i - 2])
        return steps[n - 1]
