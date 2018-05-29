# https://leetcode.com/problems/merge-intervals/description/
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key=lambda x: x.start)
        i = 0
        while i < len(intervals) - 1:
            # For each pair i, i + 1
            if intervals[i].end >= intervals[i + 1].start:
                intervals[i].end = max(intervals[i].end, intervals[i + 1].end)
                del intervals[i + 1]
            else:
                i += 1
        return intervals
