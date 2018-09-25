# https://leetcode.com/problems/number-of-boomerangs/description/
from collections import defaultdict

class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # Use a dict to count the number of different dist between i, j
        distance = [{} for _ in xrange(len(points))]
        for i in xrange(len(points) - 1):
            x_i, y_i = points[i]
            for j in xrange(i + 1, len(points)):
                x_j, y_j = points[j]
                cur_dist = ((x_i - x_j) ** 2 + (y_i - y_j) ** 2) ** 0.5
                for each in (i, j):
                    if cur_dist in distance[each]:
                        distance[each][cur_dist] += 1
                    else:
                        distance[each][cur_dist] = 1

        count = 0
        for each_dict in distance:
            for each_dist in each_dict:
                if each_dict[each_dist] > 1:
                    count += each_dict[each_dist] * (each_dict[each_dist] - 1)

        return count


    def numberOfBoomerangs_v2(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        count = 0
        for i in range(len(points)):
            x_i, y_i = points[i]
            i_dist_dict = defaultdict(int)
            for j in range(len(points)):
                if i == j: continue
                x_j, y_j = points[j]
                cur_dist = (x_i - x_j) ** 2 + (y_i - y_j) ** 2
                i_dist_dict[cur_dist] += 1

            for _, v in i_dist_dict.items():
                if v > 1:
                    # More than 1 lines connect to i share the same distance
                    # nP2 to count the permutation of number
                    # nP2 = n(n-1)
                    count += v * (v - 1)
        return count

