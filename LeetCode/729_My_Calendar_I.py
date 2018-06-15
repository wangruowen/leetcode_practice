# https://leetcode.com/problems/my-calendar-i/description/
import bisect

class MyCalendar:

    def __init__(self):
        self.starts = []
        self.booking = {}

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        # Binary Search Tree
        if start in self.starts:
            return False

        slot = bisect.bisect(self.starts, start)
        if slot > 0:
            left = self.starts[slot - 1]
            if self.booking[left] > start:
                return False
        if slot < len(self.starts):
            right = self.starts[slot]
            if end > right:
                return False
        self.starts.insert(slot, start)
        self.booking[start] = end
        return True





# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)