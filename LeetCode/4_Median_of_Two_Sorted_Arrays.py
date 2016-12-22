# https://leetcode.com/problems/median-of-two-sorted-arrays/

import math

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) <= len(nums2):
            self.short_one, self.long_one = nums1, nums2
        else:
            self.short_one, self.long_one = nums2, nums1
        self.is_odd = True if (len(self.short_one) + len(self.long_one)) % 2 == 1 else False

        return self.findMedianHelper(0, len(self.short_one) - 1, 0, len(self.long_one) - 1)


    def findMedianHelper(self, start1, end1, start2, end2):
        mid1 = self.getMedian(self.short_one, start1, end1)
        mid2 = self.getMedian(self.long_one, start2, end2)

        if start1 == end1 and start2 == end2:
            # We get to the stop point
            if self.is_odd:
                return mid1 if mid1 > mid2 else mid2
            else:
                return (mid1 + mid2) / 2.0

        if mid1 < mid2:
            new_start1 = int(math.ceil((start1 + end1) / 2.0))
            new_end2 = int(math.floor((start2 + end2) / 2.0))
            self.findMedianHelper(new_start1, end1,
                                      start2, new_end2)
        elif mid1 > mid2:
            new_end1 = int(math.floor((start1 + end1) / 2.0))
            new_start2 = int(math.ceil((start2 + end2) / 2.0))
            self.findMedianHelper(start1, new_end1,
                                  new_start2, end2)
        else:
            return mid1


    def getMedian(self, array, start_index, end_index):
        if start_index == end_index:
            return array[start_index]

        is_odd = True if (end_index - start_index) % 2 == 0 else False
        mid = (start_index + end_index) / 2
        if is_odd:
            return float(array[mid])
        else:
            return (array[mid] + array[mid + 1]) / 2.0
