# https://leetcode.com/problems/count-of-smaller-numbers-after-self/
import bisect

class Solution:
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Backward Binary Search O(n^2)
        counts = []
        sorted_ones = []
        for each in nums[::-1]:
            counts.append(bisect.bisect_left(sorted_ones, each))
            bisect.insort(sorted_ones, each)
        return counts[::-1]
