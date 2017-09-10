# https://leetcode.com/problems/first-bad-version/
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def findBadVersionInRange(self, start, end):
        mid = (start + end) / 2
        if start == mid:
            if isBadVersion(mid):
                return mid
            elif isBadVersion(end):
                return end
            else:
                return -1

        if isBadVersion(mid):
            return self.findBadVersionInRange(start, mid)
        else:
            return self.findBadVersionInRange(mid + 1, end)

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.findBadVersionInRange(1, n)

