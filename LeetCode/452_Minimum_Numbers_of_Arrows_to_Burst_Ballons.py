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

    def findMinArrowShots_v2(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0

        # No need to sort by end, just sort by start normally,
        # then keep an overlap range, if the new point can fall in the overlap
        # range, then we can still use previous arrow to shoot, otherwise
        # we have to use a new arrow, which will become a new overlap
        points.sort(key=lambda x: x[0])
        overlap_s, overlap_e = points[0]
        result = 1
        for i in range(1, len(points)):
            cur_s, cur_e = points[i]
            if overlap_e < cur_s:
                # No overlap
                result += 1
                overlap_s, overlap_e = cur_s, cur_e
            else:
                # Has overlap, then update the overlap with new point
                overlap_s = max(overlap_s, cur_s)
                overlap_e = min(overlap_e, cur_e)
        return result


