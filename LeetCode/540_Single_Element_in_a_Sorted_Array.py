# https://leetcode.com/problems/single-element-in-a-sorted-array/description/
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # A better way is Binary Search
        result = 0
        for each in nums:
            result ^= each
        return result

    def singleNonDuplicate_binary(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Total number should be odd, because only one is single
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if mid > 0 and nums[mid] == nums[mid - 1]:
                if (mid - left) % 2 == 0:
                    # left side is even, since nums[mid] == nums[mid-1],
                    # there must be a single value
                    right = mid - 2
                else:
                    # left side is odd, the right side must have a single value
                    left = mid + 1
            elif mid < len(nums) - 1 and nums[mid] == nums[mid + 1]:
                if (right - mid) % 2 == 0:
                    # right side is even, apart from the mid equal one,
                    # the right rest is odd, there must be a single value
                    left = mid + 2
                else:
                    right = mid - 1
            elif 0 < mid < len(nums) - 1:
                # nums[mid-1] != nums[mid] != nums[mid+1]
                return nums[mid]
        return nums[left]


s = Solution()
# a = [1, 1, 2, 2, 4, 4, 5, 5, 9]
a = [1,1,2]
print(s.singleNonDuplicate_binary(a))