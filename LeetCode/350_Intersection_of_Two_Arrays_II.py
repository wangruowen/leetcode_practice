# https://leetcode.com/problems/intersection-of-two-arrays-ii/description/
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # 1. Use set
        result = []
        shared_set = set(nums1).intersection(set(nums2))
        for each in shared_set:
            result.extend([each] * min(nums1.count(each), nums2.count(each)))
        return result

    def v2(self, nums1, nums2):
        # 2. sorted with two pointers
        nums1.sort()
        nums2.sort()
        i, j = 0, 0
        result = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1

        return result