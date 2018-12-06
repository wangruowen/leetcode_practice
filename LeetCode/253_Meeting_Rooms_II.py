# https://leetcode.com/problems/meeting-rooms-ii/
# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

from functools import cmp_to_key

class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        # Use positive number to indicate start, use negative number to indicate end
        # put both start and end into one list and sort it by abs
        times = []
        for x in intervals:
            times.append(x.start)
            times.append(-x.end)

        def my_cmp(x, y):
            if abs(x) < abs(y):
                return -1
            elif abs(x) > abs(y):
                return 1
            else:
                return x - y

        times.sort(key=cmp_to_key(my_cmp))

        rooms = 0
        max_rooms = 0
        for each in times:
            if each >= 0:
                rooms += 1
                max_rooms = max(max_rooms, rooms)
            else:
                rooms -= 1
        return max_rooms


    def minMeetingRooms_v2(self, intervals):
        import heapq
        intervals.sort(key=lambda x:x.start)
        heap = []  # stores the end time of intervals
        for i in intervals:
            if heap and i.start >= heap[0]:
                # means two intervals can use the same room
                heapq.heapreplace(heap, i.end)
            else:
                # a new room is allocated
                heapq.heappush(heap, i.end)
        return len(heap)
    
s = Solution()
