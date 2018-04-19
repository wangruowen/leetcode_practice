# https://leetcode.com/problems/largest-triangle-area/description/
class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        # Brute force, not interesting
        max_area = 0
        for i in xrange(len(points) - 2):
            x_i, y_i = points[i]
            for j in xrange(i + 1, len(points) - 1):
                x_j, y_j = points[j]
                vx_1, vy_1 = x_j - x_i, y_j - y_i
                for k in xrange(j + 1, len(points)):
                    x_k, y_k = points[k]
                    vx_2, vy_2 = x_k - x_i, y_k - y_i
                    # We use vector cross product to calculate area
                    area = abs(vx_1 * vy_2 - vx_2 * vy_1) / 2.0
                    max_area = max(max_area, area)

        return max_area
