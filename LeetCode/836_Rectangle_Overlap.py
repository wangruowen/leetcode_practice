# https://leetcode.com/problems/rectangle-overlap/description/
class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        # Let's consider when there is NO overlap.
        # rec1's right <= rec2's left, or
        # rec1's left >= rec2's right, or
        # rec1's top <= rec2's bottom, or
        # rec1's bottom >= rec2's top
        if rec1[2] <= rec2[0] or rec2[2] <= rec1[0] or \
            rec1[3] <= rec2[1] or rec2[3] <= rec1[1]:
            return False
        return True