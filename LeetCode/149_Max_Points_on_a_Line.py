# https://leetcode.com/problems/max-points-on-a-line/description/
# Definition for a point.
from collections import defaultdict
# from fractions import Fraction

class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        # Just keep slope in a dict
        def gcd(a, b):
            if b == 0:
                return a
            else:
                return gcd(b, a % b)

        max_points = 0
        for i in range(len(points)):
            x_i, y_i = points[i].x, points[i].y
            same = 0
            i_slope_dict = defaultdict(lambda: 1)
            i_slope_dict['self'] = 1
            for j in range(i + 1, len(points)):
                x_j, y_j = points[j].x, points[j].y
                if x_i == x_j and y_i == y_j:
                    same += 1
                    continue
                elif x_i == x_j:
                    slope_key = 'self'
                else:
                    cur_gcd = gcd(y_j - y_i, x_j - x_i)
                    slope_key = ((y_j - y_i) // cur_gcd, (x_j - x_i) // cur_gcd)
                i_slope_dict[slope_key] += 1
            max_points = max(max_points, max(i_slope_dict.values()) + same)
        return max_points


