# https://leetcode.com/problems/first-missing-positive/description/
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Set all existing negative to zero
        has_one = False
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
            elif nums[i] == 1:
                has_one = True
        if not has_one:
            return 1

        # Now we can use -1 and nums[0] for free
        for each in nums:
            each = abs(each)
            if each <= len(nums):
                if nums[each - 1] > 0:
                    nums[each - 1] = -nums[each - 1]
                elif nums[each - 1] == 0:
                    nums[each - 1] = -1

        max_num = 0
        for i in range(len(nums)):
            if i > 0 and nums[i] >= 0:
                return i + 1
            max_num = max(max_num, abs(nums[i]))

        # if all nums are negative, then the next max
        return max_num + 1

s = Solution()
a = [0,2,2,4,0,1,0,1,3]
print(s.firstMissingPositive(a))