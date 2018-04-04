# https://leetcode.com/problems/number-of-boomerangs/description/
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

