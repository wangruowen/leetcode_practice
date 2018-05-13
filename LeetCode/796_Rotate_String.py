# https://leetcode.com/problems/rotate-string/description/
class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        # For rotate string, there is a specific feature
        # double the string A + A, any rotate string is a substring in A + A
        # we can also use sliding window over A + A to get all rotate string
        return len(A) == len(B) and B in A + A
