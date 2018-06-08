# https://leetcode.com/problems/minimum-time-difference/description/
class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        # 24 hour is 1440 minutes
        timePoints = [x.split(":") for x in timePoints]
        timePoints = [int(x[0]) * 60 + int(x[1]) for x in timePoints]
        timePoints.sort()
        min_minutes_diff = 1440
        last = timePoints[-1]
        for each in timePoints:
            tmp = abs(each - last)
            min_minutes_diff = min(tmp, 1440 - tmp, min_minutes_diff)
            last = each
        return min_minutes_diff

s = Solution()
times = ["23:59","00:00"]
print(s.findMinDifference(times))


