# https://leetcode.com/problems/median-of-two-sorted-arrays/

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
        total_nums = len(self.short_one) + len(self.long_one)
        is_odd = True if total_nums % 2 == 1 else False

        return self.findMedianHelper(0, len(self.short_one) - 1, 0, len(self.long_one) - 1)


    def findMedianHelper(self, start1, end1, start2, end2):
        # First handle stop case
        mid1 = self.getMedian(self.short_one, start1, end1)
        mid2 = self.getMedian(self.long_one, start2, end2)

        if mid1 < mid2:
            if start1 + 1 == end1:

            else:
                self.findMedianHelper((start1 + end1) / 2, end1,
                                      start2, (start2 + end2) / 2)
        elif mid1 > mid2:
            self.findMedianHelper(start1, (start1 + end1) / 2,
                                  (start2 + end2) / 2, end2)
        else:
            return mid1


    def getMedian(self, array, start_index, end_index):
        if start_index == end_index:
            return array[start_index]

        is_odd = True if (end_index - start_index) % 2 == 0 else False
        mid = (start_index + end_index) / 2
        if is_odd:
            return array[mid]
        else:
            return (array[mid] + array[mid + 1]) / 2
