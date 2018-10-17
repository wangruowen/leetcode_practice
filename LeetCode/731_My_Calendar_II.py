# https://leetcode.com/problems/my-calendar-ii/description/
# import bisect
# from collections import defaultdict

class MyCalendarTwo(object):

    def __init__(self):
        self.calendar = []
        self.overlap = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        # The bruteforce way is O(n^2) with another array keeps all overlapped one
        # Note that, this one cannot use Binary Search on start points, because it can cover
        # quite big range that needs iteration.
        for each_start, each_end in self.overlap:
            if start < each_end and each_start < end:
                return False
        for each_start, each_end in self.calendar:
            if start < each_end and each_start < end:
                self.overlap.append([max(each_start, start), min(each_end, end)])
        self.calendar.append([start, end])

        return True

s = MyCalendarTwo()
print(s.book(26, 35))
print(s.book(26, 32))
print(s.book(25, 32))
print(s.book(18, 26))
print(s.book(40, 45))
print(s.book(19, 26))





# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)