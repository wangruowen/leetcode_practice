# https://leetcode.com/problems/next-permutation/description/
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # In a Reverse way, find the first i-th item which is
        # bigger than i-1 th item
        found = False
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                found = True
                break
        if not found:
            # reverse it
            i, j = 0, len(nums) - 1
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        elif i == len(nums) - 1:
            nums[i - 1], nums[i] = nums[i], nums[i - 1]
        else:
            # Find the smallest but bigger than nums[i - 1], swap
            min_j = nums[i]
            min_j_index = i
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i - 1] and nums[j] < min_j:
                    min_j = nums[j]
                    min_j_index = j
            # Swap i - 1 and j
            nums[i - 1], nums[min_j_index] = nums[min_j_index], nums[i - 1]
            # Re-order nums[i:]
            nums[i:] = sorted(nums[i:])

        # return nums

s = Solution()
nums = [2, 3, 1]
s.nextPermutation(nums)
print(nums)