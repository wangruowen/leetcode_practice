# https://leetcode.com/problems/evaluate-division/description/
from collections import defaultdict

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        quot = defaultdict(dict)
        for i in range(len(values)):
            num, den = equations[i]
            val = values[i]
            quot[num][den] = val
            quot[den][num] = 1 / val
        for i in quot:
            # In one group, find all
            for j in quot[i]:
                for k in quot[i]:
                    quot[j][k] = quot[i][k] / quot[i][j]
                    quot[k][j] = 1 / quot[j][k]
        return [quot[x][y] if x in quot and y in quot[x] else -1.0 for x, y in queries]