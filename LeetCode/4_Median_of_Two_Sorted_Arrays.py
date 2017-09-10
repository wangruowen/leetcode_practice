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
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        total_num = m + n
        half_num = total_num / 2
        # If total_num is odd, the median index should be total_num / 2. Each side has (total_num - 1) / 2
        # If total_num is even, the median pair should be [total_num / 2 - 1, total_num / 2]. Each side has total_num / 2

        # By defining right_half_num = (total_num + 1) / 2, we can represent both odd and even case for total_num.
        # When odd, right is i + j + 1, left is i + j. When even, right and left are i + j, where i + j = (total_num + 1) / 2

        i_min, i_max = 0, m
        while i_min <= i_max:
            i = (i_min + i_max) / 2
            j = half_num - i
            if i > 0 and nums1[i - 1] > nums2[j]:
                # when i > 0, i - 1 at most 0, and if nums1[i - 1] > nums2[j], then nums1[i] >> nums2[j - 1]
                i_max = i - 1
            elif i < m and nums1[i] < nums2[j - 1]:
                # when i < m, i at most m - 1, and if nums1[i] < nums2[j - 1], then nums1[i - 1] << nums2[j]
                i_min = i + 1
            else:
                if i == 0:
                    # To the smallest nums1, but still bigger then nums2[j-1]
                    max_of_left = nums2[j - 1]
                elif j == 0:
                    # To the smallest nums2,
                    max_of_left = nums1[i - 1]
                else:
                    max_of_left = max(nums1[i - 1], nums2[j - 1])

                if i == m:
                    min_of_right = nums2[j]
                elif j == n:
                    min_of_right = nums1[i]
                else:
                    min_of_right = min(nums1[i], nums2[j])

                if total_num % 2 == 1:
                    # If odd,
                    return min_of_right
                else:
                    return (max_of_left + min_of_right) / 2.0

        return -1

    def general_binary_search(self, nums, key):
        start, end = 0, len(nums)
        while start < end:
            mid = (start + end) / 2
            # If len is odd, mid index is right in the mid
            # If len is even, mid index is the first of the right half
            if key == nums[mid]:
                print("Found key")
                return mid
            elif key < nums[mid]:
                end = mid
            else:
                # If we do start = mid, this may never end
                start = mid + 1

        return -1



a = [3, 4, 5, 6, 7, 8]
b = [0, 1, 2]

s = Solution()
print(s.findMedianSortedArrays(a, b))

print(s.general_binary_search(a, 5))
print(s.general_binary_search(b, 2))
