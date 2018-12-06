# https://leetcode.com/problems/data-stream-as-disjoint-intervals/
# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

import heapq

class SummaryRanges:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # We need to use heap to be similar to Java's TreeMap
        self.q = []
        self.key_set = set()

    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        if val not in self.key_set:
            self.key_set.add(val)
            heapq.heappush(self.q, (val, Interval(val, val)))

    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        new_q = []
        while self.q:
            cur_v, cur_int = heapq.heappop(self.q)
            if not new_q:
                new_q.append((cur_v, cur_int))
            else:
                if new_q[-1][1].end + 1 >= cur_int.start:
                    new_q[-1][1].end = max(cur_int.end, new_q[-1][1].end)
                else:
                    new_q.append((cur_v, cur_int))

        self.q = new_q
        return [x[1] for x in self.q]



# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()