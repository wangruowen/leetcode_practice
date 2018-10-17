# https://leetcode.com/problems/find-right-interval/description/
# Definition for an interval.
import bisect

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        # Hashmap + Binary Search
        start2index = {x.start: i for i, x in enumerate(intervals)}
        starts = sorted([x.start for x in intervals])
        result = []
        for each in intervals:
            i = bisect.bisect_left(starts, each.end)
            result.append(start2index[starts[i]] if i < len(starts) else -1)
        return result



s = Solution()
inter = []
inter.append(Interval(3,4))
inter.append(Interval(2,3))
inter.append(Interval(1,2))
print(s.findRightInterval(inter))
