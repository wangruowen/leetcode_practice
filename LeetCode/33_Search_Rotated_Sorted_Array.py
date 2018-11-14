class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 1:
            return -1

        # First, let's find the pivot's index
        pivot, pivot_val = self._get_pivot(nums)
        start_val, end_val = nums[0], nums[-1]
        # Second, now we basically check whether the target is at the left half or the right half
        if target == pivot_val:
            return pivot
        elif target >= start_val and pivot > 0 and target <= nums[pivot - 1]:
            return self._binary_search(nums[:pivot], target)
        elif target > pivot_val and pivot < len(nums) - 1 and target <= end_val:
            tmp_index = self._binary_search(nums[pivot + 1:], target)
            if tmp_index != -1:
                return tmp_index + pivot + 1
            else:
                return -1
        else:
            return -1

    def _get_pivot(self, nums):
        start, end = 0, len(nums)
        while start < end:
            mid = (start + end) / 2
            if mid > 0 and nums[mid] < nums[mid - 1]:
                return mid, nums[mid]
            elif nums[mid] < nums[start]:
                # pivot is between start and mid
                end = mid
            elif nums[mid] > nums[end - 1]:
                if start == mid:
                    # only two values, start, start + 1
                    return start + 1, nums[start + 1]
                else:
                    start = mid
            else:
                break

        return 0, nums[0]

    def _binary_search(self, nums, target):
        start, end = 0, len(nums)
        while start < end:
            mid = (start + end) / 2
            if target < nums[mid]:
                end = mid
            elif target > nums[mid]:
                start = mid + 1
            else:
                return mid
        return -1

    def search_v2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1

        # Two cases,
        # 1. Target is in the ordered half
        # 2. Target is in the half with pivot
        def helper(start, end):
            """
            start inclusive, end exclusive
            """
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            if start == mid:
                return -1

            if nums[start] < nums[mid]:
                # this part is ordered
                if nums[start] <= target < nums[mid]:
                    return helper(start, mid)
                else:
                    # target should be in the pivot part
                    return helper(mid, end)
            else:
                # nums[start] > nums[mid], which has pivot
                if nums[mid] < target <= nums[end - 1]:
                    return helper(mid, end)
                else:
                    # target should be in the pivot part
                    return helper(start, mid)
        return helper(0, len(nums))

    def search_iterative(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[left] and nums[left] <= target < nums[mid] or \
                nums[mid] < nums[left] and not (nums[mid] < target <= nums[right]):
                right = mid - 1
            else:
                left = mid + 1
        return -1

s = Solution()
# a = [1, 3]
# target = 2
a = [5, 1, 3]
target = 3
# print("Pivot: %d, Value: %d" % (s._get_pivot(a)))
print("Target '%d' is located at %d" % (target, s.search_v2(a, target)))
