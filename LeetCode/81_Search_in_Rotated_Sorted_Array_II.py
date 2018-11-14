# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
class Solution:
    def find_pivot_not_working_with_dups(self, nums):
        # Eventually, pivot should be found in two-item array
        # array[0] > array[1]
        start, end = 0, len(nums)
        while start < end:
            mid = (start + end) // 2
            if start == mid:
                if nums[start] > nums[start + 1]:
                    return start + 1, nums[start + 1]
                break

            if mid > 0 and nums[mid] < nums[mid - 1]:
                return mid, nums[mid]
            elif nums[mid] < nums[start]:
                # pivot is between start and mid
                end = mid
            elif nums[mid] > nums[end - 1]:
                # pivot is between mid and end
                start = mid
            elif nums[start] == nums[mid] == nums[end - 1]:
                # Special case for duplicates
                start += 1
                end -= 1
            else:
                # No pivot found
                break

        # If pivot not found, the array is sorted, return the first
        return 0, nums[0]

    def search_not_working_with_dups(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if len(nums) < 2:
            return target in nums

        # It is possible that [2,2,2,3,4,0,1,2,2], we need to find pivot first
        # Then we do binary search on one side of the pivot
        pivot_index, pivot = self.find_pivot(nums)
        print(pivot_index, pivot)
        start, end = 0, len(nums)
        if pivot_index > 0:
            if target < nums[0]:
                # target should be found after the pivot
                start = pivot_index
            else:
                # target should be found before the pivot
                end = pivot_index
        # Then we just do regular binary search
        while start < end:
            mid = (start + end) // 2
            if target < nums[mid]:
                end = mid
            elif target > nums[mid]:
                start = mid + 1
            else:
                return True
        return False

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if len(nums) == 0:
            return False
        pivot = nums[0]
        if target == pivot:
            return True

        # Dup happens when left and right are equal
        # !!key!!
        # we move lo and hi so pivot will never equal to lo or hi
        left, right = 0, len(nums) - 1
        while left < len(nums) and nums[left] == pivot:
            left += 1
        while right >= 0 and nums[right] == pivot:
            right -= 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] < pivot:
                if nums[mid] < target < pivot:
                    left = mid + 1
                else:
                    right = mid - 1
            elif nums[mid] > pivot:
                if pivot < target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        return False


s = Solution()
# nums = [2,2,2,3,4,0,1,2,2]
nums = [1,1,1,3,1]
print(s.search(nums, 3))