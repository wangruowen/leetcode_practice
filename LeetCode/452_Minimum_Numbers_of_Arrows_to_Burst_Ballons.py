# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/
class Solution:
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # Greedy order by ending position and shoot the end
        points.sort(key=lambda x: x[1])
        last_shoot = None
        shoots = 0
        for start, end in points:
            if last_shoot:
                if start <= last_shoot <= end:
                    continue
            last_shoot = end
            shoots += 1
        return shoots



