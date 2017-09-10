class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last = None
        for i in nums:
            if last == None:
                last = i
            else:
                if last > i:
                    return i
                else:
                    last = i

        return nums[0]

    def findMin_v2(self, nums):
        """
        Use binary search
        :param nums:
        :return:
        """
        start, end = 0, len(nums) - 1
        # If end is within the array index, we usually use "start <= end" in while condition,
        # instead of "start < end"
        while start <= end:
            mid = (start + end) / 2
            if mid > 0 and nums[mid - 1] > nums[mid]:
                return nums[mid]

            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid - 1

        return nums[0]


s = Solution()
print(s.findMin_v2([4, 5, 6, 7, 0, 1, 2]))
