# https://leetcode.com/problems/meeting-rooms/
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        last = None
        intervals.sort(key=lambda x: x.start)
        for x in intervals:
            if last and x.start < last.end:
                return False
            last = x
        return True
