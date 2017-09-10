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


s = Solution()
a = [1, 3]
target = 2
print("Pivot: %d, Value: %d" % (s._get_pivot(a)))
print("Target '%d' is located at %d" % (target, s.search(a, target)))
