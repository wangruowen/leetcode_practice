# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/description/
class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # https://leetcode.com/problems/shortest-unsorted-continuous-subarray/discuss/103066/Ideas-behind-the-O(n)-two-pass-and-one-pass-solutions
        # Backward, get the min of subarray starting from current item
        # Forward, get the max of subarray ending with current item
        # Then,
        # Forward, if current item bigger than current min, that is the start point
        # Backward, If current item smaller than current max, that is the end point
        cur_min_array = [float('inf') for _ in range(len(nums))]
        cur_max_array = [float('-inf') for _ in range(len(nums))]
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                cur_min_array[i] = nums[i]
            else:
                cur_min_array[i] = min(cur_min_array[i+1], nums[i])
        for i in range(len(nums)):
            if i == 0:
                cur_max_array[i] = nums[i]
            else:
                cur_max_array[i] = max(cur_max_array[i-1], nums[i])
        start = 0
        while start < len(nums):
            if nums[start] > cur_min_array[start]:
                break
            else:
                start += 1
        if start == len(nums):
            return 0

        end = len(nums) - 1
        while end >= 0:
            if nums[end] < cur_max_array[end]:
                break
            else:
                end -= 1
        if end < 0:
            return 0

        return end - start + 1

s = Solution()
nums = [2, 6, 4, 8, 10, 9, 15]
print(s.findUnsortedSubarray(nums))

