# https://leetcode.com/problems/median-of-two-sorted-arrays/
# For this question, we actually cannot separately deal with two arrays, because we may get lost in even/odd numbers.
# The following solution is kinda wrong.

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

        return self.findMedianHelper(0, len(self.short_one), 0, len(self.long_one))


    def findMedianHelper(self, start1, end1, start2, end2):
        if end1 - start1 <= 3 and end2 - start2 <= 3:
            return self.solveSimpleCase(start1, end1, start2, end2)
        else:
            mid1_index, mid2_index = (start1 + end1) / 2, (start2 + end2) / 2
            mid1, mid2 = self.short_one[mid1_index], self.long_one[mid2_index]

            # If start + end is even,
            # return the mid as the first item in the second half of the array;
            # If start + end is odd,
            # return the exact mid item of the array
            if mid1 < mid2:
                return self.findMedianHelper(mid1_index, end1, start2, mid2_index)
            elif mid1 > mid2:
                return self.findMedianHelper(start1, mid1_index, mid2_index, end2)
            else:
                return mid1


    def solveSimpleCase(self, start1, end1, start2, end2):
        if end1 - start1 == 0:
            tmp1 = self.short_one[start1:(start1 + 1)]
        else:
            tmp1 = self.short_one[start1:end1]
        if end2 - start2 == 0:
            tmp2 = self.long_one[start2:(start2 + 1)]
        else:
            tmp2 = self.long_one[start2:end2]
        tmp = sorted(tmp1 + tmp2)
        mid = tmp[len(tmp) / 2] if len(tmp) % 2 == 1 else (tmp[len(tmp) / 2 - 1] + tmp[len(tmp) / 2]) / 2.0

        return float(mid)


a = [3,4,5,6,7,8]
b = [0, 1, 2]

s = Solution()
print(s.findMedianSortedArrays(a, b))