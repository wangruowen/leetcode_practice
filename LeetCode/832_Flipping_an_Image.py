# https://leetcode.com/problems/flipping-an-image/description/
class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for _ in range(len(A)):
            one_line = A.pop(0)
            A.append([1-x for x in one_line[::-1]])
        return A



